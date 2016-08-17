import seaborn as sn
import numpy as np
import pandas as pd

clust_files = [x for x in os.listdir() if x.endswith('.1D')]
clust_nums = [x.split('_')[1] for x  in clust_files]
clust_df = pd.DataFrame([clust_nums,clust_files]).T

def cust_factorplot(x, y, hue, data, kind, palette, ax=None)
    fig = sn.plt.figure(figsize=(6,4))
    ax = fig.add_subplot(111)
    vel = sn.factorplot(x='prox',y='weight',hue='vel',data=vel_df, kind='bar', palette=np.array(sn.color_palette())[[0,2]], ax=ax)
    sn.plt.close()
    ax.set_axis_bgcolor('white')
    ax.spines['bottom'].set_color('black')
    ax.set_xlabel("")
    ax.set_ylabel("weight")
    ax.set_title('{}:\nVelocity Binned by Proximity'.format(cluster_name.replace('_', ' ').title()), ha='center')
    return fig

def plot_cluster(num, cluster_name):
    vel = cust_factorplot(x='prox',y='weight',hue='vel',data=vel_df, kind='bar', palette=np.array(sn.color_palette())[[0,2]], ax=ax1)
    #vel.savefig('vel_{}.jpg'.format(cluster_name))
    prox = cust_factorplot(x='vel',y='weight',hue='prox',data=prox_df, kind='bar', palette=np.array(sn.color_palette())[[1,3]], ax=ax2)
    #prox.savefig('vel_{}.jpg'.format(cluster_name))
