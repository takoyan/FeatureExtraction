import module.Calclator
import pandas as pd

class FeatureExtraction():
    def get_features(df, i, window):
        ROUND = 1000
        new_df = pd.DataFrame()
        df_all = df[(df['unixTime'] // ROUND >= ((df['unixTime'].min() // ROUND) + i - window)) & (
                    df['unixTime'] // ROUND <= ((df['unixTime'].min() // ROUND) + i))]

        df_acc = df_all[df_all['type'] == 'Accelerometer']
        df_gyro = df_all[df_all['type'] == 'Gyroscope']
        if len(df_acc) == 0 or len(df_gyro) == 0:
            return new_df

        acc_x_ave, acc_y_ave, acc_z_ave, acc_range, acc_x_std, acc_y_std, acc_z_std, gyro_range, \
        gyro_x_ave, gyro_y_ave, gyro_z_ave, gyro_x_std, gyro_y_std, gyro_z_std, acc_std, gyro_std, \
        acc_skewness, gyro_skewness, acc_kurtosis, gyro_kurtosis, acc_energy, gyro_energy, acc_ave, gyro_ave = \
        module.Calclator.get_Ave_value(df_acc['x']), module.Calclator.get_Ave_value(df_acc['y']), module.Calclator.get_Ave_value(df_acc['z']), module.Calclator.get_Range(df_acc), \
        module.Calclator.get_Std_value(df_acc['x']), module.Calclator.get_Std_value(df_acc['y']), module.Calclator.get_Std_value(df_acc['z']), module.Calclator.get_Range(df_gyro), \
        module.Calclator.get_Ave_value(df_gyro['x']), module.Calclator.get_Ave_value(df_gyro['y']), module.Calclator.get_Ave_value(df_gyro['z']), module.Calclator.get_Std_value(df_gyro['x']), \
        module.Calclator.get_Std_value(df_gyro['y']), module.Calclator.get_Std_value(df_gyro['z']), module.Calclator.get_Std(df_acc), module.Calclator.get_Std(df_gyro), module.Calclator.get_Skewness(df_acc), \
        module.Calclator.get_Skewness(df_gyro), module.Calclator.get_Kurtosis(df_acc), module.Calclator.get_Kurtosis(df_gyro), module.Calclator.get_Energy(df_acc), module.Calclator.get_Energy(df_gyro), module.Calclator.get_ave(df_acc), module.Calclator.get_ave(df_gyro)

        new_df = new_df.append(
            {'acc_x_ave_window{}'.format(window): acc_x_ave, 'acc_y_ave_window{}'.format(window): acc_y_ave,
             'acc_z_ave_window{}'.format(window): acc_z_ave,
             'acc_range_window{}'.format(window): acc_range, 'acc_x_std_window{}'.format(window): acc_x_std,
             'acc_y_std_window{}'.format(window): acc_y_std, 'acc_z_std_window{}'.format(window): acc_z_std,
             'gyro_range_window{}'.format(window): gyro_range,
             'gyro_x_ave_window{}'.format(window): gyro_x_ave, 'gyro_y_ave_window{}'.format(window): gyro_y_ave,
             'gyro_z_ave_window{}'.format(window): gyro_z_ave, 'gyro_x_std_window{}'.format(window): gyro_x_std,
             'gyro_y_std_window{}'.format(window): gyro_y_std, 'gyro_z_std_window{}'.format(window): gyro_z_std,
             'acc_std_window{}'.format(window): acc_std, 'gyro_std_window{}'.format(window): gyro_std,
             'acc_skewness_window{}'.format(window): acc_skewness,
             'gyro_skewness_window{}'.format(window): gyro_skewness,
             'acc_kurtosis_window{}'.format(window): acc_kurtosis,
             'gyro_kurtosis_window{}'.format(window): gyro_kurtosis, 'acc_energy_window{}'.format(window): acc_energy,
             'gyro_energy_window{}'.format(window): gyro_energy, 'acc_ave_window{}'.format(window): acc_ave,
             'gyro_ave_window{}'.format(window): gyro_ave},
            ignore_index=True)

        return new_df

    def featureExtraction(self, file_name):
        all_df = pd.DataFrame()

        df = pd.read_json("../raw_data/"+file_name+".json".format(file_name), orient='records', lines=True)

        print('{}LOAD DONE!!!!'.format(file_name))

        for i in range(5, (df['unixTime'][len(df["unixTime"])-1]//1000)-(df['unixTime'][0]//1000)+1, 1):
            new_df = pd.DataFrame()
            for window in range(0, 4):
                features = self.get_features(df, i, window)
                if len(features) == 0:
                    continue
                new_df = pd.concat([new_df, features], axis=1)
            all_df = all_df.append(new_df)

        all_df.to_csv("../features/{}.csv".format(file_name), index=False)
        print('{}DONE!!!!'.format(file_name))

"""
if __name__=="__main__":
    fe = FeatureExtraction()
    fe.featureExtraction('./', '5NM4tiger')
"""