async function fetchData() {
    try {
        const response = await fetch('https://api.myjson.com/bins/1gwnal');
        const data = await response.json();
        console.log(data);
        // Далее код для вставки данных в HTML
    } catch (error) {
        console.error('Ошибка при получении данных:', error);
    }
}

fetchData();


