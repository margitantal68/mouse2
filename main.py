import plot_paper
import balabit_statistics as bs
import plot_actions_session


import settings as st
import twoclass_classification as tc
import user_accuracies as ua
import rawdata2actions as rd
import feature_selection as fs
import plot_paper as pp

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# SESSION_CUT = 1
def main_ACTION_SEQUENCE():
    st.SESSION_CUT = 1
    st.CASE = 'training'
    print("***Computing training features")
    rd.process_files(st.CASE)
    print('***Evaluating on the test set')
    st.CASE = 'test'
    rd.process_files(st.CASE)
    tc.NUM_NEGATIVE_SAMPLES_PER_CLASS = 70
    tc.NUM_POSITIVE_SAMPLES = 630
    tc.evaluate_test_actions2(st.TRAINING_FEATURE_FILENAME, st.TEST_FEATURE_FILENAME)
    return


# SESSION_CUT = 2
def main_ACTION():
    st.SESSION_CUT = 2
    print("***Computing training features")
    st.CASE = 'training'
    rd.process_files( st.CASE )
    print('***Evaluating on the test set')
    st.CASE = 'test'
    rd.process_files(st.CASE)
    print('EVAL_TEST_UNIT: '+str(st.EVAL_TEST_UNIT))
    tc.NUM_NEGATIVE_SAMPLES_PER_CLASS = 200
    tc.NUM_POSITIVE_SAMPLES = 1800
    if st.EVAL_TEST_UNIT == 0:
        # evaluation: all actions from a session
        tc.evaluate_test_session(st.TRAINING_FEATURE_FILENAME, st.TEST_FEATURE_FILENAME)
    else:
        # evaluation: action by action
        tc.evaluate_test_actions(st.TRAINING_FEATURE_FILENAME, st.TEST_FEATURE_FILENAME,
                                                      st.NUM_EVAL_ACTIONS)
    return


# SESSION_CUT = 2
# def main_ACTION_USER_ACC_TRAINING():
#     st.SESSION_CUT = 2
#     print("***Computing training features")
#     st.CASE = 'training'
#     rd.process_files( st.CASE )
#     print('***Evaluating on the test set')
#     tc.NUM_NEGATIVE_SAMPLES_PER_CLASS = 200
#     tc.NUM_POSITIVE_SAMPLES = 1800
#     tc.evaluate_training( st.TRAINING_FEATURE_FILENAME )
#     return
#
#
# # SESSION_CUT = 1
# def main_ACTION_SEQUENCE_USER_ACC_TRAINING():
#     st.SESSION_CUT = 1
#     print("***Computing training features")
#     st.CASE = 'training'
#     rd.process_files( st.CASE )
#     print('***Evaluating on the test set')
#     tc.NUM_NEGATIVE_SAMPLES_PER_CLASS = 70
#     tc.NUM_POSITIVE_SAMPLES = 630
#     tc.evaluate_training( st.TRAINING_FEATURE_FILENAME )
#     return


# main_ACTION_SEQUENCE()
# main_ACTION()

# usertestscores.csv
# ua.user_accuracies('output/usertestscores.csv')

# bs.session_action_statistics(st.TRAINING_FEATURE_FILENAME)
# pp.plotScoresCase1()
# pp.plotUserHistograms()

# plot_actions_session.plot_all_actions_sesssion('output/balabit_features_test.csv', 'user12', '1178629549')
plot_actions_session.plot_all_actions_sesssion+('output/balabit_features_training.csv', 'user12', '2144641057')


# # OLD  main
# def main( case ):
#     if case == 'training':
#         print("Compute training features")
#         rd.process_files( case )
#         twoclass_classification.evaluate_training(st.TRAINING_FEATURE_FILENAME)
#     else:
#         print("Compute test features")
#         rd.process_files( case )
#         if st.SESSION_CUT == 2:
#             if st.EVAL_TEST_UNIT==0:
#                 # evaluation: all actions from a session
#                 twoclass_classification.evaluate_test_session(st.TRAINING_FEATURE_FILENAME, st.TEST_FEATURE_FILENAME)
#             else:
#                 # evaluation: action by action
#                 twoclass_classification.evaluate_test_actions(st.TRAINING_FEATURE_FILENAME, st.TEST_FEATURE_FILENAME, st.NUM_EVAL_ACTIONS )
#         else:
#             # SESSION_CUT=1, each test session --> one feature vector in the test feature file
#             twoclass_classification.evaluate_test_actions2(st.TRAINING_FEATURE_FILENAME, st.TEST_FEATURE_FILENAME)
#             # twoclass_classification.evaluate_test_actions(st.TRAINING_FEATURE_FILENAME, st.TEST_FEATURE_FILENAME, 1)
#     return
