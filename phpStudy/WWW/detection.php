<?php
$array = $_POST['packet'];
$cmd = "python script/run.py " . $array;
# echo $cmd;
$output = shell_exec($cmd);
# $array = explode("\n", $output);
# echo $output;
# print_r($array);
# foreach ($array as $value) {
# echo $value . "</br>";
# }

$file = 'script/test.txt';
$cbody = file($file); 
for($i=0;$i<count($cbody);$i++){ 
  echo $cbody[$i];
  echo "<br/>";
}
?> 
