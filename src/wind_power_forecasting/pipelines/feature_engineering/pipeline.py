from kedro.pipeline import Pipeline, node
from typing import Dict
from .nodes import feature_engineering, show_feature_importance, save_prepared_data


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=feature_engineering,
                inputs=[
                    "params:wf",
                    "params:folder.pri",
                    "params:add_time_feat",
                    "params:add_cycl_feat",
                    "params:add_inv_T",
                ],
                outputs=["X_train_pped", "X_test_pped", "feature_names",],
                name="feature_engineering",
            ),
            node(
                func=save_prepared_data,
                inputs=[
                    "params:folder.fea",
                    "X_train_pped",
                    "X_test_pped",
                    "params:wf",
                ],
                outputs=None,
                name="save_prepared_data",
            ),
            node(
                func=show_feature_importance,
                inputs=[
                    "params:wf",
                    "params:folder.pri",
                    "X_train_pped",
                    "feature_names",
                    "params:k_best",
                ],
                outputs=None,
                name="feature_selection",
            ),
        ],
        tags="feature_engineering",
    )
