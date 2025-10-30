(function () {
  const display = document.getElementById('display');
  const keys = document.querySelector('.keys');
  const error = document.getElementById('error');

  let firstOperand = null;
  let pendingOp = null;
  let overwrite = true;

  function setError(msg) {
    error.textContent = msg || '';
  }

  function setDisplay(value) {
    display.value = value;
  }

  function parseDisplay() {
    const v = display.value.replace(',', '.');
    return Number(v);
  }

  function inputDigit(d) {
    setError('');
    if (overwrite || display.value === '0') {
      setDisplay(d);
      overwrite = false;
    } else {
      setDisplay(display.value + d);
    }
  }

  function inputDot() {
    setError('');
    if (overwrite) {
      setDisplay('0.');
      overwrite = false;
      return;
    }
    if (!display.value.includes('.')) setDisplay(display.value + '.');
  }

  function clearAll() {
    firstOperand = null;
    pendingOp = null;
    overwrite = true;
    setDisplay('0');
    setError('');
  }

  function applyOp(op, a, b) {
    switch (op) {
      case '+': return a + b;
      case '-': return a - b;
      case '*': return a * b;
      case '/':
        if (b === 0) {
          throw new Error('Деление на ноль');
        }
        return a / b;
      default: return b;
    }
  }

  function chooseOp(op) {
    setError('');
    const current = parseDisplay();
    if (pendingOp === null) {
      firstOperand = current;
    } else if (!overwrite) {
      try {
        firstOperand = applyOp(pendingOp, firstOperand, current);
        setDisplay(String(firstOperand));
      } catch (e) {
        setError(e.message);
      }
    }
    pendingOp = op;
    overwrite = true;
  }

  function equals() {
    if (pendingOp === null) return;
    const current = parseDisplay();
    try {
      const result = applyOp(pendingOp, firstOperand, current);
      setDisplay(String(result));
      firstOperand = result;
      pendingOp = null;
      overwrite = true;
      setError('');
    } catch (e) {
      setError(e.message);
    }
  }

  function toggleSign() {
    if (display.value === '0') return;
    if (display.value.startsWith('-')) setDisplay(display.value.slice(1));
    else setDisplay('-' + display.value);
  }

  function toPercent() {
    const v = parseDisplay();
    setDisplay(String(v / 100));
  }

  keys.addEventListener('click', (e) => {
    const btn = e.target.closest('button');
    if (!btn) return;
    const action = btn.getAttribute('data-action');
    const text = btn.textContent;

    if (!action) {
      if (text === '.') inputDot();
      else inputDigit(text);
      return;
    }

    switch (action) {
      case 'clear':
        clearAll();
        break;
      case 'op':
        chooseOp(btn.getAttribute('data-op'));
        break;
      case 'equals':
        equals();
        break;
      case 'sign':
        toggleSign();
        break;
      case 'percent':
        toPercent();
        break;
      default:
        break;
    }
  });
  clearAll();
})();


