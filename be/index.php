// This is the admin login homepage.

<!DOCTYPE html>
<html>
<head>
<title>Admin Login</title>
</head>
<body>

    <?php
      //calling python script
      $command = escapeshellcmd('/usr/custom/search.py');
      $output = shell_exec($command);
      echo $output;

      include "relative/path/to/your/firstfile.html";
      include "relative/path/to/your/secondfile.html";
      include "relative/path/to/your/evenwithothersuffix/thirdfile.php";
      include "relative/path/to/your/fourth/file/in/another/folder.html";
    ?>

</body>
</html> 
