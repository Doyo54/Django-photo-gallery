copyToClipboard=(value) => {
    navigator.clipboard.writeText(value);
    alert("Url copied successfully. Paste it after the default url -https://gallery-doyo.herokuapp.com ");
          }