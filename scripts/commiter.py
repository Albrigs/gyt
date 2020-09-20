from os import system

def commit(emo1, emo2, title, body, stage_all=0):
    all = stage_all*"-a"
    system(f"git commit {all} -m\"{emo1}{emo2}{title}\" -m \"{body}\" ")
