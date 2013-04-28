<?php    
    // now greet the caller
    header("content-type: text/xml");
    echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n";
?>
<Response>
    <Say>Hello.</Say>
    <Gather numDigits="1" action="choose-key.php" method="POST">
        <Say>
            For the next slide, press 3.
            For the previous slide, press 1.
            To pause, press 0.
        </Say>
    </Gather>
</Response>