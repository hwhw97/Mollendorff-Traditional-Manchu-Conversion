async function loadPyodideAndScript() {
    window.pyodide = await loadPyodide();
    await pyodide.loadPackage(["micropip"]);
    await pyodide.runPythonAsync(`
        import sys
        import micropip
        sys.path.append(".")  # 确保可以导入本地 Python 文件
    `);

    // 读取 Python 代码并执行
    let response = await fetch("convert_manscript.py");
    let pythonCode = await response.text();
    await pyodide.runPythonAsync(pythonCode);
}

// 运行 Pyodide 并加载 Python 代码
loadPyodideAndScript();

async function convert() {
    let inputText = document.getElementById("inputText").value;
    if (!inputText.trim()) {
        alert("请输入文本进行转换！");
        return;
    }

    // 调用 Python 的 convert_manscript() 函数
    let outputText = await pyodide.runPythonAsync(`
        convert_manscript(${JSON.stringify(inputText)})
    `);

    document.getElementById("outputText").innerText = outputText;
}