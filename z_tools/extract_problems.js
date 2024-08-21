const results = [];
document.querySelectorAll('div[role="row"]').forEach(row => {
    const linkElement = row.querySelector('a[href*="/problems/"]');
    if (linkElement) {
        const url = linkElement.getAttribute('href');
        const title = linkElement.textContent.trim();
        results.push({ url, title });
    }
});
console.log(results);
