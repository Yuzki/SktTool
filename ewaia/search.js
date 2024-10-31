let jsonData;

// JSON ファイルを読み込む
fetch('data.json')
    .then(response => response.json())
    .then(data => {
        jsonData = data;
    })
    .catch(error => console.error('JSONの読み込みエラー:', error));

// 正規表現での検索を実行
function search() {
    const searchField = document.getElementById('searchField').value;
    const searchInput = document.getElementById('searchInput').value;
    const regex = new RegExp(searchInput, 'i');
    const resultsContainer = document.getElementById('results');
    resultsContainer.innerHTML = '';

    if (!jsonData) {
        resultsContainer.innerHTML = '<p>No JSON data</p>';
        return;
    }

    Object.keys(jsonData).forEach(rootKey => {
        const entry = jsonData[rootKey];
        let match = false;

        // 検索条件に応じてフィルター
        if (searchField === 'key' && regex.test(rootKey)) match = true;
        if (searchField === 'meaningDe' && entry.meaning.deu.some(de => regex.test(de))) match = true;
        if (searchField === 'meaningJp' && entry.meaning.jpn.some(jp => regex.test(jp))) match = true;
        if (searchField === 'verbForm' && entry.verb.some(verb => regex.test(verb.form))) match = true;
        if (searchField === 'nounForm' && entry.noun.some(noun => regex.test(noun.form))) match = true;

        // マッチした結果を表示
        if (match) {
            const resultDiv = document.createElement('div');
            resultDiv.classList.add('result');

            // キー、it、pieを表示
            resultDiv.innerHTML = `<div class="result-key">${rootKey}</div>`;
            resultDiv.innerHTML += `<div><strong>it:</strong> ${entry.it}</div>`;
            resultDiv.innerHTML += `<div><strong>pie:</strong> ${entry.pie}</div>`;

            // meaning (deu, jpn) 表示
            const meaningDiv = document.createElement('div');
            meaningDiv.innerHTML = `<strong>Meaning:</strong><br><em>German:</em> ${entry.meaning.deu.join(', ')}<br><em>Japanese:</em> ${entry.meaning.jpn.join(', ')}`;
            resultDiv.appendChild(meaningDiv);

            // verb 表示
            entry.verb.forEach(verb => {
                const verbDiv = document.createElement('div');
                verbDiv.innerHTML = `<strong>Verb:</strong> ${verb.form} (${verb.morph}) - Literature: ${verb.literature.join(', ')}`;
                resultDiv.appendChild(verbDiv);
            });

            // noun 表示
            entry.noun.forEach(noun => {
                const nounDiv = document.createElement('div');
                nounDiv.innerHTML = `<strong>Noun:</strong> ${noun.form} - Meaning: ${noun.meaning} - Literature: ${noun.literature.join(', ')}`;
                resultDiv.appendChild(nounDiv);
            });

            resultsContainer.appendChild(resultDiv);
        }
    });
}
