const printerError = s => `${s.match(/[n-z]/g)?.length ?? "0"}/${s.length}`;
