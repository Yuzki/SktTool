function displayButton() {
    const searchInput = document.getElementById('searchInput');
    const displayButton = document.getElementById('displayButton');
    const pageSelector = document.getElementById('pageSelector');

    displayButton.addEventListener('click', () => {
        const word = searchInput.value;
        const { BOOK, PAGE } = getBookAndPageFromWord(word);
        displaySelectedWordAndPage(BOOK, PAGE);
    });

    pageSelector.addEventListener('change', () => {
        const selectedPage = pageSelector.value;
        const word = searchInput.value;
        displayImage(word, selectedPage);
    });

    searchInput.addEventListener('input', () => {
        const query = searchInput.value;
        const matchedWords = search(query);

        // 検索結果を表示
        const suggestions = document.getElementById('suggestions');
        suggestions.innerHTML = '';
        matchedWords.forEach(({ word, pages }) => {
            const li = document.createElement('li');
            li.textContent = word;
            li.addEventListener('click', () => {
                searchInput.value = word; // クリックした単語を検索窓に表示
                updatePageSelector(pages);
            });
            suggestions.appendChild(li);
        });
    });
}

function updatePageSelector(pages) {
    const pageSelector = document.getElementById('pageSelector');
    pageSelector.innerHTML = '';
    pages.forEach(page => {
        const option = document.createElement('option');
        option.value = page;
        option.textContent = page;
        pageSelector.appendChild(option);
    });
}

function displaySelectedWordAndPage(BOOK, PAGE) {
    const selectedWordAndPage = document.getElementById('selectedWordAndPage');
    selectedWordAndPage.textContent = `Selected Word: ${searchInput.value}, Page: ${BOOK}_${PAGE}`;
}

function displayImage(BOOK, PAGE) {
    const imagePath = `img/${BOOK}_${PAGE}.png`;
    const image = new Image();
    image.src = imagePath;

    // Viewer.js の初期化と画像の追加
    const viewer = new Viewer(document.getElementById('displayedImage'), {
        title: book, // 画像のタイトルとして書籍名を設定
        url: imagePath,
        navbar: false, // ナビゲーションバー非表示
        toolbar: {
            zoomIn: 4, // ズームイン倍率
            zoomOut: 4, // ズームアウト倍率
            oneToOne: true, // 1:1 表示を許可
            reset: true, // リセットボタンを表示
            prev: true, // 前の画像ボタンを表示
            play: false, // スライドショー再生ボタン非表示
            next: true, // 次の画像ボタンを表示
            rotateLeft: false, // 左回転ボタン非表示
            rotateRight: false, // 右回転ボタン非表示
            flipHorizontal: false, // 水平反転ボタン非表示
            flipVertical: false, // 垂直反転ボタン非表示
        },
    });

    viewer.show(); // 画像を表示
}
