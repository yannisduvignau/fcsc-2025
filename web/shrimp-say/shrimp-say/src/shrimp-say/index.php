<?php

function redirect($msg, $bg)
{
  header("Location: /?msg=$msg&bg=$bg");
  die();
}

if (!isset($_GET['msg'])) {
  redirect("Hello Shrimp", "lightblue");
}

$msg = $_GET['msg'] ?? "Hello World";
$bg = $_GET['bg'] ?? "lightblue";



if (strpos($msg, "<") !== false) {
  redirect("NO XSS", "red");
}

?>
<!DOCTYPE html>
<html>

<head>
  <link rel="icon" href="data:,">
  <style>
    
    body {
      background-color: <?= htmlentities($bg) ?>;
    }
    
    .speech-bubble {
      position: relative;
      background: #f0f0f0;
      color: #333;
      padding: 15px;
      width: 200px;
      border-radius: 10px;
      text-align: center;
      font-family: Arial, sans-serif;
      font-size: 16px;
      box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
      transform: translate(80px);
    }

    /* The tail of the speech bubble */
    .speech-bubble::after {
      content: "";
      position: absolute;
      bottom: -20px;
      /* Adjust this to position the tail */
      left: 20px;
      /* Moves tail left or right */
      border-width: 10px;
      border-style: solid;
      border-color: #f0f0f0 transparent transparent transparent;
      display: block;
    }

    body {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }

    img {
      width: 20vw;
      image-rendering: pixelated  ;
      z-index: 10;
    }
  </style>
</head>

<body>
  <main>
    <div class="speech-bubble"></div>
    <img src="/shrimp.gif" alt="Shrimp">
  </main>
  <script type="text/base64" id="data"><?= base64_encode($msg) ?></script>
  <script>
    document.querySelector(".speech-bubble").innerHTML = atob(document.getElementById('data').innerText)
  </script>
</body>

</html>