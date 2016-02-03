<?php

//exec('git --git-dir=.git pull');
//exec('git fetch');
//exec('git reset --hard origin/master');

exec('git --git-dir=.git fetch >> error.log');
exec('git --git-dir=.git reset --hard origin/master >> error.log');


exec('chmod -R 755 ./*');
echo 'Called by githubHookTest';

?>
