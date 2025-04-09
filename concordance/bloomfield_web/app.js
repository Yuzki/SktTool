document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('search-button').addEventListener('click', performSearch);
});

function performSearch() {
    const searchInput = document.getElementById('search-input').value;
    const selectedTransliteration = document.getElementById('transliteration-select').value;

    // bloomfield-vc.json ファイルのデータを読み込む
    fetch('https://raw.githubusercontent.com/epicfaace/sanskrit/a851ac7bb739d7fc7379315e3d211b9ac3e1b3c5/dcs/data/bloomfield-vedic-concordance/data/bloomfield-vc.json')
        .then(response => response.json())
        .then(concData => {
            // transliteration.csv ファイルのデータを読み込む
            fetch('https://raw.githubusercontent.com/Yuzki/SktTool/master/utils/transliteration.csv')
                .then(response => response.text())
                .then(transliterationCsv => {
                    const transliterationData = parseCsv(transliterationCsv);

                    // 検索実行
                    const results = searchInData(searchInput, selectedTransliteration, concData, transliterationData);

                    // 結果表示
                    displayResults(results, transliterationData);
                });
        });
}

function parseCsv(csv) {
    return csv.split('\n')
        .map(line => line.split(','))
        .filter(row => row.length > 1 && row.every(field => field.trim() !== ''));
}

function transliterateSearchInput(searchInput, inputTransliteration, outputTransliteration, transliterationData) {
    const transliterationMap = {};

    const inputIndex = transliterationData[0].indexOf(inputTransliteration);
    const outputIndex = transliterationData[0].indexOf(outputTransliteration);
    console.log(`Input index: ${inputIndex}, Output index: ${outputIndex}`);

    if (inputIndex === -1 || outputIndex === -1) {
        console.error(`Invalid transliteration types: ${inputTransliteration}, ${outputTransliteration}`);
        return searchInput;
    }

    transliterationData.slice(1).forEach(row => {
        // console.log(`Row: ${row}`);
        // console.log(`Input: ${row[inputIndex]}, Output: ${row[outputIndex]}`);
        transliterationMap[row[inputIndex]] = row[outputIndex];
    });

    console.log(transliterationMap);

    let result = searchInput;

    for (const key in transliterationMap) {
        const value = transliterationMap[key];
        result = result.replace(key, value);
    }

    return result;
}

function searchInData(query, selectedTransliteration, concData, transliterationData) {
    const iastSearchInput = transliterateSearchInput(query, selectedTransliteration, "iast", transliterationData);

    const concResults = concData
        .flatMap(item => item.cits.map(cit => ({ text: `${item.mantra} (${cit.cit})`, type: 'Conc' })))
        .filter(result => {
            if (selectedTransliteration === 'tf') {
                return result.text.includes(iastSearchInput);
            } else {
                const regex = new RegExp(iastSearchInput, 'g');
                return regex.test(result.text);
            }
        });

    return [iastSearchInput, concResults];
}

function displayResults(results, transliterationData) {
    const resultContainer = document.getElementById('result-container');
    resultContainer.innerHTML = '';

    const searchString = results[0];
    const searchResults = results[1];

    if (searchResults.length === 0) {
        resultContainer.innerHTML = `<div class="alert alert-info mt-3">No results found for ${searchString}</div>`;
        return;
    }

    // searchStringを先頭に追加
    const resultItem = document.createElement('div');
    resultItem.classList.add('card', 'mt-3');

    const header = document.createElement('div');
    header.classList.add('card-header');
    header.textContent = `Results for ${searchString}`;

    const body = document.createElement('div');
    body.classList.add('card-body');

    searchResults.forEach(result => {
        const iastText = result.text;
        console.log(iastText);
        const isoText = transliterateSearchInput(iastText, 'iast', 'iso', transliterationData);
        const resultText = document.createElement('p');
        resultText.textContent = isoText;
        body.appendChild(resultText);
    });

    resultItem.appendChild(header);
    resultItem.appendChild(body);
    resultContainer.appendChild(resultItem);
}
