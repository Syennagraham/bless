import subprocess
PASSWORD = 'abc123'
BLESSCAKEY = 'TESTS'
BLESSCONFIGDIR = 'lambda_configs'

PRIVATEKEY = './' + BLESSCONFIGDIR + '/' +  BLESSCAKEY
subprocess.Popen(["ssh-keygen", "-t", "rsa", "-N", PASSWORD, "-b", "4096", "-f", PRIVATEKEY])
