<?php

$connection = new MongoClient();
$db = $connection -> ABC_Book_Store;
$collection = $db->Invoices;


$json = array(json_decode(file_get_contents("php://input")));
/*var_dump($json);die();*/

$collection->insert($json);


?>