<?php

/*if(isset($_POST['uploadfile'])) {
    $target_path = "data/";
    echo("1");
    $target_path = $target_path.basename($_FILES['uploadfile']['name']);
    echo("2");

    if (move_uploaded_file($_FILES['uplaodfile']['tmp_name'], $target_path)) {
        echo "The file" . basename($_FILES['uplaodfile']['name']) . "has been uploaded";
    } else {
        echo "There is a error in uploading";
    }
}*/

$my_folder = "data/";

if (move_uploaded_file($_FILES['file']['tmp_name'], $my_folder . $_FILES['file']['name'])) {
    echo 'Received file' . $_FILES['file']['name'] . ' with size ' . $_FILES['file']['size'];
} else {
    echo 'Upload failed!';

    var_dump($_FILES['file']['error']);
}

?>