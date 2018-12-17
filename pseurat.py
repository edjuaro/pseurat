import subprocess

def log(message,extra='==>'):
    print(extra,message)
    return


def execute(comando, doitlive=True, input_to_use=None, verbose=True):
    # result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
    comando = comando.split(' ')

    if doitlive:
        popen = subprocess.Popen(comando, stdout=subprocess.PIPE, universal_newlines=True)

        to_return = popen.stdout.read()
        for line in to_return:
            if verbose:  # I see no reason to doitlive and have it be not verbose, but to each their own.
                print(line, end='')
        popen.stdout.close()
        return_code = popen.wait()
        if return_code:
            raise subprocess.CalledProcessError(return_code, comando)
    else:
        if input_to_use is not None:
            input_to_use = input_to_use.ecode('utf-8')
        result = subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, input=input_to_use)

        to_return = result.stdout.decode('utf-8')
        if verbose:
            print(to_return)
    return to_return.strip('\n')


def run_R(command, rcript='temp_rscript.R', rlog='temp.log', writelog=False):
    with open(rcript, 'w') as f:
        f.write(command)
    if writelog:
        print("Running an R command, this may take a while and will only print output at the end of the run.")
        subprocess.call(f'Rscript {rcript} > {rlog} 2>&1 || cat {rlog}', shell=True)

        with open(rlog, 'r') as f:
            for line in f.readlines():
                print(line)
    else:
        print("Running the R command as an Rscript and printing the output as it becomes available.")
        execute(f'Rscript {rcript}')
    return
