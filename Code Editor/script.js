
function selectOption(option) {
  document.getElementById('dropdown-button').innerHTML = option + '<span class="dropdown-arrow">&#9660;</span>';
}

require.config({ paths: { 'vs': 'https://cdn.jsdelivr.net/npm/monaco-editor@0.27.0/min/vs' }});

require(['vs/editor/editor.main'], function() {
  var editor = monaco.editor.create(document.getElementById('editorContainer'), {
    value: 'console.log("Hi");',
    language: 'javascript',
    theme: 'vs-dark',
    automaticLayout: true
  });

  document.getElementById('convertbutton').addEventListener('click', function() {
    var userCode = editor.getValue();
    var selectedLanguage = document.getElementById('dropdown-button').innerText;

    var apiUrl = `http://localhost:8080/chat?prompt=Act like a professional developer , Don't give any introduction just show the code and convert the given code  ${encodeURIComponent(userCode)} into language=${encodeURIComponent(selectedLanguage)}`;

    fetch(apiUrl)
      .then(response => response.text())
      .then(apiResponse => {
        var resultContainer = document.getElementById('resultContainer');
        resultContainer.innerText = apiResponse;
      })
      .catch(error => {
        console.error('API Request Error:', error);
      });
  });

  document.getElementById('debugbutton').addEventListener('click', function() {
    var userCode = editor.getValue();
    var selectedLanguage = document.getElementById('dropdown-button').innerText;

    var apiUrl = `http://localhost:8080/chat?prompt=Act like a professional developer , Don't give any introduction and debug the given code  ${encodeURIComponent(userCode)}`;

    fetch(apiUrl)
      .then(response => response.text())
      .then(apiResponse => {
        var resultContainer = document.getElementById('resultContainer');
        resultContainer.innerText = apiResponse;
      })
      .catch(error => {
        console.error('API Request Error:', error);
      });
  });

  document.getElementById('qualitybutton').addEventListener('click', function() {
    var userCode = editor.getValue();
    var selectedLanguage = document.getElementById('dropdown-button').innerText;

    var apiUrl = `http://localhost:8080/chat?prompt=Act like a professional developer , Don't give any introduction and check quality of  the given code  ${encodeURIComponent(userCode)} and provide result in just 80-90  words and you can provide answer in points`;

    fetch(apiUrl)
      .then(response => response.text())
      .then(apiResponse => {
        var resultContainer = document.getElementById('resultContainer');
        resultContainer.innerText = apiResponse;
      })
      .catch(error => {
        console.error('API Request Error:', error);
      });
  });


});









  
 











 


     
      
      
      
      
