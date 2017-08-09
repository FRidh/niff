import pytest

#NIFF_EXECUTABLE = 'niff'
#"""The path to the executable.
#"""

URLS = [

    ]



def run(cmd):
    """Run `cmd`.
    """
    output = subprocess.check_output(cmd, universal_newlines=True)
    return output.rstrip().split('\n')


@pytest.mark.xfail(reason='PR branches are occasionally removed.')
def test_command_pr():

    # Note that often people remove branches so this test will fail.
    pr = 28184
    run('niff pr pr://{pr}')
    run('niff pr {pr}')





