<?php
const VOLUME = './messages';
$msg = $_POST['msg'];

$files = scandir(VOLUME);
$files_index = count($files) - 2;

$file_name = "$files_index.txt";
$file = fopen(VOLUME . "/$file_name", "w");
fwrite($file, $msg);
fclose($file);

header("Location: index.php");
