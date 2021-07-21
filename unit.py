import os
import cfg


def makedirs(path):
    if not os.path.exists(path):
        os.makedirs(path)


if __name__ == '__main__':
    out = 'train/'
    makedirs(out)
    i_t_dir = os.path.join(out, cfg.i_t_dir)
    i_s_dir = os.path.join(out, cfg.i_s_dir)
    t_sk_dir = os.path.join(out, cfg.t_sk_dir)
    t_t_dir = os.path.join(out, cfg.t_t_dir)
    t_b_dir = os.path.join(out, cfg.t_b_dir)
    t_f_dir = os.path.join(out, cfg.t_f_dir)
    mask_t_dir = os.path.join(out, cfg.mask_t_dir)

    makedirs(i_t_dir)
    makedirs(i_s_dir)
    makedirs(t_sk_dir)
    makedirs(t_t_dir)
    makedirs(t_b_dir)
    makedirs(t_f_dir)
    makedirs(mask_t_dir)

    with open('unit_paths.txt', "r") as f:
        for line in f:
            dir = line.strip()
            paths = os.listdir(dir)
            for path in paths:
                for file in os.listdir(dir + path):
                    os.replace(dir + path + '/' + file, out + path + '/' + str(dir).replace('/', '_') + '_' + file)
