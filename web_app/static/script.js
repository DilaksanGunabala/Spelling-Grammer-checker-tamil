function checkGrammar() {
    const input = document.getElementById('grammarInput').value;
    fetch('/check_grammar', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `sentence=${encodeURIComponent(input)}`
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('grammarOutput').innerText = `Suggested Correction: ${data.suggestion}`;
        });
}

function checkSpelling() {
    const input = document.getElementById('spellingInput').value;
    fetch('/check_spelling', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `word=${encodeURIComponent(input)}`
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('spellingOutput').innerText = `Suggested Correction: ${data.suggestion}`;
        });
}
