<?php
 
    // if the caller pressed anything but 1 or 2 send them back
    if($_REQUEST['Digits'] != '1' and $_REQUEST['Digits'] != '2') {
        header("Location: prompt.php");
        die;
    }
     
    header("content-type: text/xml");
    echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n";
?>
<Response>
<?php if ($_REQUEST['Digits'] == '1') { ?>
    <Gather action="/process_gather.php" method="GET"></Gather>
<?php } elseif ($_REQUEST['Digits'] == '3') { ?>
    <Gather action="/process_gather.php" method="GET"></Gather>
<?php } ?>
</Response> 
