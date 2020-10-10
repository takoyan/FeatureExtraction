import module.Calclator
import pandas as pd

class FeatureExtraction():
    def featureExtraction(self, file_name):
        ROUND = 1000

        new_df = pd.DataFrame()
        df = pd.read_json("../raw_data/"+file_name+'.json', orient='records', lines=True)

        print('{}LOAD DONE!!!!'.format(file_name))

        for i in range(5, (df['unixTime'][len(df["unixTime"])-1]//1000)-(df['unixTime'][0]//1000)+1, 1):
            df_all = df[df['unixTime'] // ROUND == ((df['unixTime'].min() // ROUND) + i)]
            df_acc = df_all[df_all['type'] == 'Accelerometer']
            df_gyro = df_all[df_all['type'] == 'Gyroscope']

            df_old_all = df[df['unixTime'] // ROUND == ((df['unixTime'].min() // ROUND) + i - 1)]
            df_old_acc = df_old_all[df_old_all['type'] == 'Accelerometer']
            df_old_gyro = df_old_all[df_old_all['type'] == 'Gyroscope']

            if len(df_acc) == 0 or len(df_gyro) == 0:
                continue

            old_acc_x_ave, old_acc_y_ave, old_acc_z_ave, old_acc_range, old_acc_x_std, old_acc_y_std, old_acc_z_std, old_gyro_range, \
            old_gyro_x_ave, old_gyro_y_ave, old_gyro_z_ave, old_gyro_x_std, old_gyro_y_std, old_gyro_z_std, old_acc_std, old_gyro_std, \
            old_acc_skewness, old_gyro_skewness, old_acc_kurtosis, old_gyro_kurtosis, old_acc_energy, old_gyro_energy, old_acc_ave, old_gyro_ave = \
            module.Calclator.get_Ave_value(df_old_acc['x']), module.Calclator.get_Ave_value(df_old_acc['y']), module.Calclator.get_Ave_value(df_old_acc['z']), module.Calclator.get_Range(df_old_acc), \
            module.Calclator.get_Std_value(df_old_acc['x']), module.Calclator.get_Std_value(df_old_acc['y']), module.Calclator.get_Std_value(df_old_acc['z']), module.Calclator.get_Range(df_old_gyro), \
            module.Calclator.get_Ave_value(df_old_gyro['x']), module.Calclator.get_Ave_value(df_old_gyro['y']), module.Calclator.get_Ave_value(df_old_gyro['z']), module.Calclator.get_Std_value(df_old_gyro['x']), \
            module.Calclator.get_Std_value(df_old_gyro['y']), module.Calclator.get_Std_value(df_old_gyro['z']), module.Calclator.get_Std(df_old_acc), module.Calclator.get_Std(df_old_gyro), module.Calclator.get_Skewness(df_old_acc), \
            module.Calclator.get_Skewness(df_old_gyro), module.Calclator.get_Kurtosis(df_old_acc), module.Calclator.get_Kurtosis(df_old_gyro), module.Calclator.get_Energy(df_old_acc), module.Calclator.get_Energy(df_old_gyro), module.Calclator.get_ave(df_old_acc), module.Calclator.get_ave(df_old_gyro)

            acc_x_ave, acc_y_ave, acc_z_ave, acc_range, acc_x_std, acc_y_std, acc_z_std, gyro_range, \
            gyro_x_ave, gyro_y_ave, gyro_z_ave, gyro_x_std, gyro_y_std, gyro_z_std, acc_std, gyro_std, \
            acc_skewness, gyro_skewness, acc_kurtosis, gyro_kurtosis, acc_energy, gyro_energy, acc_ave, gyro_ave = \
            module.Calclator.get_Ave_value(df_acc['x']), module.Calclator.get_Ave_value(df_acc['y']), module.Calclator.get_Ave_value(df_acc['z']), module.Calclator.get_Range(df_acc), \
            module.Calclator.get_Std_value(df_acc['x']), module.Calclator.get_Std_value(df_acc['y']), module.Calclator.get_Std_value(df_acc['z']), module.Calclator.get_Range(df_gyro), \
            module.Calclator.get_Ave_value(df_gyro['x']), module.Calclator.get_Ave_value(df_gyro['y']), module.Calclator.get_Ave_value(df_gyro['z']), module.Calclator.get_Std_value(df_gyro['x']), \
            module.Calclator.get_Std_value(df_gyro['y']), module.Calclator.get_Std_value(df_gyro['z']), module.Calclator.get_Std(df_acc), module.Calclator.get_Std(df_gyro), module.Calclator.get_Skewness(df_acc), \
            module.Calclator.get_Skewness(df_gyro), module.Calclator.get_Kurtosis(df_acc), module.Calclator.get_Kurtosis(df_gyro), module.Calclator.get_Energy(df_acc), module.Calclator.get_Energy(df_gyro), module.Calclator.get_ave(df_acc), module.Calclator.get_ave(df_gyro)

            new_df = new_df.append({'acc_x_ave': acc_x_ave, 'acc_y_ave': acc_y_ave,
                                    'acc_z_ave': acc_z_ave,
                                    'acc_range': acc_range, 'acc_x_std': acc_x_std, 'acc_y_std': acc_y_std,
                                    'acc_z_std': acc_z_std, 'gyro_range': gyro_range,
                                    'gyro_x_ave': gyro_x_ave, 'gyro_y_ave': gyro_y_ave, 'gyro_z_ave': gyro_z_ave,
                                    'gyro_x_std': gyro_x_std,
                                    'gyro_y_std': gyro_y_std, 'gyro_z_std': gyro_z_std, 'acc_std': acc_std,
                                    'gyro_std': gyro_std, 'acc_skewness': acc_skewness,
                                    'gyro_skewness': gyro_skewness, 'acc_kurtosis': acc_kurtosis,
                                    'gyro_kurtosis': gyro_kurtosis, 'acc_energy': acc_energy,
                                    'gyro_energy': gyro_energy, 'acc_ave': acc_ave, 'gyro_ave': gyro_ave,
                                    'dif_acc_x_ave': (acc_x_ave - old_acc_x_ave), 'dif_acc_y_ave': (acc_y_ave - old_acc_y_ave),
                                    'dif_acc_z_ave': (acc_z_ave - old_acc_z_ave),
                                    'dif_acc_range': (acc_range - old_acc_range), 'dif_acc_x_std': (acc_x_std - old_acc_x_std),
                                    'dif_acc_y_std': (acc_y_std - old_acc_y_std), 'dif_acc_z_std': (acc_z_std - old_acc_z_std),
                                    'dif_gyro_range': (gyro_range - old_gyro_range),
                                    'dif_gyro_x_ave': (gyro_x_ave - old_gyro_x_ave),
                                    'dif_gyro_y_ave': (gyro_y_ave - old_gyro_y_ave),
                                    'dif_gyro_z_ave': (gyro_z_ave - old_gyro_z_ave),
                                    'dif_gyro_x_std': (gyro_x_std - old_gyro_x_std),
                                    'dif_gyro_y_std': (gyro_y_std - old_gyro_y_std),
                                    'dif_gyro_z_std': (gyro_z_std - old_gyro_z_std), 'dif_acc_std': (acc_std - old_acc_std),
                                    'dif_gyro_std': (gyro_std - old_gyro_std),
                                    'dif_acc_skewness': (acc_skewness - old_acc_skewness),
                                    'dif_gyro_skewness': (gyro_skewness - old_gyro_skewness),
                                    'dif_acc_kurtosis': (acc_kurtosis - old_acc_kurtosis),
                                    'dif_gyro_kurtosis': (gyro_kurtosis - old_gyro_kurtosis),
                                    'dif_acc_energy': (acc_energy - old_acc_energy),
                                    'dif_gyro_energy': (gyro_energy - old_gyro_energy), 'dif_acc_ave': (acc_ave - old_acc_ave),
                                    'dif_gyro_ave': (gyro_ave - old_gyro_ave)},
                                   ignore_index=True)

        new_df.to_csv("./features/{}.csv".format(file_name), index=False)
        print('{}DONE!!!!'.format(file_name))

"""
if __name__=="__main__":
    fe = FeatureExtraction()
    fe.featureExtraction('./', '5NM4tiger')
"""