# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'DatasetImportJobDataSourcePropertiesArgs',
    'DatasetImportJobArgs',
    'SolutionCategoricalHyperParameterRangeArgs',
    'SolutionConfigAutoMLConfigPropertiesArgs',
    'SolutionConfigHpoConfigPropertiesAlgorithmHyperParameterRangesPropertiesArgs',
    'SolutionConfigHpoConfigPropertiesHpoObjectivePropertiesArgs',
    'SolutionConfigHpoConfigPropertiesHpoResourceConfigPropertiesArgs',
    'SolutionConfigHpoConfigPropertiesArgs',
    'SolutionConfigArgs',
    'SolutionContinuousHyperParameterRangeArgs',
    'SolutionIntegerHyperParameterRangeArgs',
]

@pulumi.input_type
class DatasetImportJobDataSourcePropertiesArgs:
    def __init__(__self__, *,
                 data_location: Optional[pulumi.Input[str]] = None):
        """
        The Amazon S3 bucket that contains the training data to import.
        :param pulumi.Input[str] data_location: The path to the Amazon S3 bucket where the data that you want to upload to your dataset is stored.
        """
        if data_location is not None:
            pulumi.set(__self__, "data_location", data_location)

    @property
    @pulumi.getter(name="dataLocation")
    def data_location(self) -> Optional[pulumi.Input[str]]:
        """
        The path to the Amazon S3 bucket where the data that you want to upload to your dataset is stored.
        """
        return pulumi.get(self, "data_location")

    @data_location.setter
    def data_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_location", value)


@pulumi.input_type
class DatasetImportJobArgs:
    def __init__(__self__, *,
                 data_source: Optional[pulumi.Input['DatasetImportJobDataSourcePropertiesArgs']] = None,
                 dataset_arn: Optional[pulumi.Input[str]] = None,
                 dataset_import_job_arn: Optional[pulumi.Input[str]] = None,
                 job_name: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None):
        """
        Initial DatasetImportJob for the created dataset
        :param pulumi.Input['DatasetImportJobDataSourcePropertiesArgs'] data_source: The Amazon S3 bucket that contains the training data to import.
        :param pulumi.Input[str] dataset_arn: The ARN of the dataset that receives the imported data
        :param pulumi.Input[str] dataset_import_job_arn: The ARN of the dataset import job
        :param pulumi.Input[str] job_name: The name for the dataset import job.
        :param pulumi.Input[str] role_arn: The ARN of the IAM role that has permissions to read from the Amazon S3 data source.
        """
        if data_source is not None:
            pulumi.set(__self__, "data_source", data_source)
        if dataset_arn is not None:
            pulumi.set(__self__, "dataset_arn", dataset_arn)
        if dataset_import_job_arn is not None:
            pulumi.set(__self__, "dataset_import_job_arn", dataset_import_job_arn)
        if job_name is not None:
            pulumi.set(__self__, "job_name", job_name)
        if role_arn is not None:
            pulumi.set(__self__, "role_arn", role_arn)

    @property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> Optional[pulumi.Input['DatasetImportJobDataSourcePropertiesArgs']]:
        """
        The Amazon S3 bucket that contains the training data to import.
        """
        return pulumi.get(self, "data_source")

    @data_source.setter
    def data_source(self, value: Optional[pulumi.Input['DatasetImportJobDataSourcePropertiesArgs']]):
        pulumi.set(self, "data_source", value)

    @property
    @pulumi.getter(name="datasetArn")
    def dataset_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the dataset that receives the imported data
        """
        return pulumi.get(self, "dataset_arn")

    @dataset_arn.setter
    def dataset_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dataset_arn", value)

    @property
    @pulumi.getter(name="datasetImportJobArn")
    def dataset_import_job_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the dataset import job
        """
        return pulumi.get(self, "dataset_import_job_arn")

    @dataset_import_job_arn.setter
    def dataset_import_job_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dataset_import_job_arn", value)

    @property
    @pulumi.getter(name="jobName")
    def job_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name for the dataset import job.
        """
        return pulumi.get(self, "job_name")

    @job_name.setter
    def job_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "job_name", value)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the IAM role that has permissions to read from the Amazon S3 data source.
        """
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_arn", value)


@pulumi.input_type
class SolutionCategoricalHyperParameterRangeArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Provides the name and values of a Categorical hyperparameter.
        :param pulumi.Input[str] name: The name of the hyperparameter.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] values: A list of the categories for the hyperparameter.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if values is not None:
            pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the hyperparameter.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of the categories for the hyperparameter.
        """
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "values", value)


@pulumi.input_type
class SolutionConfigAutoMLConfigPropertiesArgs:
    def __init__(__self__, *,
                 metric_name: Optional[pulumi.Input[str]] = None,
                 recipe_list: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The AutoMLConfig object containing a list of recipes to search when AutoML is performed.
        :param pulumi.Input[str] metric_name: The metric to optimize.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] recipe_list: The list of candidate recipes.
        """
        if metric_name is not None:
            pulumi.set(__self__, "metric_name", metric_name)
        if recipe_list is not None:
            pulumi.set(__self__, "recipe_list", recipe_list)

    @property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> Optional[pulumi.Input[str]]:
        """
        The metric to optimize.
        """
        return pulumi.get(self, "metric_name")

    @metric_name.setter
    def metric_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metric_name", value)

    @property
    @pulumi.getter(name="recipeList")
    def recipe_list(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of candidate recipes.
        """
        return pulumi.get(self, "recipe_list")

    @recipe_list.setter
    def recipe_list(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "recipe_list", value)


@pulumi.input_type
class SolutionConfigHpoConfigPropertiesAlgorithmHyperParameterRangesPropertiesArgs:
    def __init__(__self__, *,
                 categorical_hyper_parameter_ranges: Optional[pulumi.Input[Sequence[pulumi.Input['SolutionCategoricalHyperParameterRangeArgs']]]] = None,
                 continuous_hyper_parameter_ranges: Optional[pulumi.Input[Sequence[pulumi.Input['SolutionContinuousHyperParameterRangeArgs']]]] = None,
                 integer_hyper_parameter_ranges: Optional[pulumi.Input[Sequence[pulumi.Input['SolutionIntegerHyperParameterRangeArgs']]]] = None):
        """
        The hyperparameters and their allowable ranges
        :param pulumi.Input[Sequence[pulumi.Input['SolutionCategoricalHyperParameterRangeArgs']]] categorical_hyper_parameter_ranges: The categorical hyperparameters and their ranges.
        :param pulumi.Input[Sequence[pulumi.Input['SolutionContinuousHyperParameterRangeArgs']]] continuous_hyper_parameter_ranges: The continuous hyperparameters and their ranges.
        :param pulumi.Input[Sequence[pulumi.Input['SolutionIntegerHyperParameterRangeArgs']]] integer_hyper_parameter_ranges: The integer hyperparameters and their ranges.
        """
        if categorical_hyper_parameter_ranges is not None:
            pulumi.set(__self__, "categorical_hyper_parameter_ranges", categorical_hyper_parameter_ranges)
        if continuous_hyper_parameter_ranges is not None:
            pulumi.set(__self__, "continuous_hyper_parameter_ranges", continuous_hyper_parameter_ranges)
        if integer_hyper_parameter_ranges is not None:
            pulumi.set(__self__, "integer_hyper_parameter_ranges", integer_hyper_parameter_ranges)

    @property
    @pulumi.getter(name="categoricalHyperParameterRanges")
    def categorical_hyper_parameter_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SolutionCategoricalHyperParameterRangeArgs']]]]:
        """
        The categorical hyperparameters and their ranges.
        """
        return pulumi.get(self, "categorical_hyper_parameter_ranges")

    @categorical_hyper_parameter_ranges.setter
    def categorical_hyper_parameter_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SolutionCategoricalHyperParameterRangeArgs']]]]):
        pulumi.set(self, "categorical_hyper_parameter_ranges", value)

    @property
    @pulumi.getter(name="continuousHyperParameterRanges")
    def continuous_hyper_parameter_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SolutionContinuousHyperParameterRangeArgs']]]]:
        """
        The continuous hyperparameters and their ranges.
        """
        return pulumi.get(self, "continuous_hyper_parameter_ranges")

    @continuous_hyper_parameter_ranges.setter
    def continuous_hyper_parameter_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SolutionContinuousHyperParameterRangeArgs']]]]):
        pulumi.set(self, "continuous_hyper_parameter_ranges", value)

    @property
    @pulumi.getter(name="integerHyperParameterRanges")
    def integer_hyper_parameter_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SolutionIntegerHyperParameterRangeArgs']]]]:
        """
        The integer hyperparameters and their ranges.
        """
        return pulumi.get(self, "integer_hyper_parameter_ranges")

    @integer_hyper_parameter_ranges.setter
    def integer_hyper_parameter_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SolutionIntegerHyperParameterRangeArgs']]]]):
        pulumi.set(self, "integer_hyper_parameter_ranges", value)


@pulumi.input_type
class SolutionConfigHpoConfigPropertiesHpoObjectivePropertiesArgs:
    def __init__(__self__, *,
                 metric_name: Optional[pulumi.Input[str]] = None,
                 metric_regex: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input['SolutionConfigHpoConfigPropertiesHpoObjectivePropertiesType']] = None):
        """
        The metric to optimize during HPO.
        :param pulumi.Input[str] metric_name: The name of the metric
        :param pulumi.Input[str] metric_regex: A regular expression for finding the metric in the training job logs.
        :param pulumi.Input['SolutionConfigHpoConfigPropertiesHpoObjectivePropertiesType'] type: The type of the metric. Valid values are Maximize and Minimize.
        """
        if metric_name is not None:
            pulumi.set(__self__, "metric_name", metric_name)
        if metric_regex is not None:
            pulumi.set(__self__, "metric_regex", metric_regex)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the metric
        """
        return pulumi.get(self, "metric_name")

    @metric_name.setter
    def metric_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metric_name", value)

    @property
    @pulumi.getter(name="metricRegex")
    def metric_regex(self) -> Optional[pulumi.Input[str]]:
        """
        A regular expression for finding the metric in the training job logs.
        """
        return pulumi.get(self, "metric_regex")

    @metric_regex.setter
    def metric_regex(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metric_regex", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input['SolutionConfigHpoConfigPropertiesHpoObjectivePropertiesType']]:
        """
        The type of the metric. Valid values are Maximize and Minimize.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input['SolutionConfigHpoConfigPropertiesHpoObjectivePropertiesType']]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class SolutionConfigHpoConfigPropertiesHpoResourceConfigPropertiesArgs:
    def __init__(__self__, *,
                 max_number_of_training_jobs: Optional[pulumi.Input[str]] = None,
                 max_parallel_training_jobs: Optional[pulumi.Input[str]] = None):
        """
        Describes the resource configuration for hyperparameter optimization (HPO).
        :param pulumi.Input[str] max_number_of_training_jobs: The maximum number of training jobs when you create a solution version. The maximum value for maxNumberOfTrainingJobs is 40.
        :param pulumi.Input[str] max_parallel_training_jobs: The maximum number of parallel training jobs when you create a solution version. The maximum value for maxParallelTrainingJobs is 10.
        """
        if max_number_of_training_jobs is not None:
            pulumi.set(__self__, "max_number_of_training_jobs", max_number_of_training_jobs)
        if max_parallel_training_jobs is not None:
            pulumi.set(__self__, "max_parallel_training_jobs", max_parallel_training_jobs)

    @property
    @pulumi.getter(name="maxNumberOfTrainingJobs")
    def max_number_of_training_jobs(self) -> Optional[pulumi.Input[str]]:
        """
        The maximum number of training jobs when you create a solution version. The maximum value for maxNumberOfTrainingJobs is 40.
        """
        return pulumi.get(self, "max_number_of_training_jobs")

    @max_number_of_training_jobs.setter
    def max_number_of_training_jobs(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "max_number_of_training_jobs", value)

    @property
    @pulumi.getter(name="maxParallelTrainingJobs")
    def max_parallel_training_jobs(self) -> Optional[pulumi.Input[str]]:
        """
        The maximum number of parallel training jobs when you create a solution version. The maximum value for maxParallelTrainingJobs is 10.
        """
        return pulumi.get(self, "max_parallel_training_jobs")

    @max_parallel_training_jobs.setter
    def max_parallel_training_jobs(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "max_parallel_training_jobs", value)


@pulumi.input_type
class SolutionConfigHpoConfigPropertiesArgs:
    def __init__(__self__, *,
                 algorithm_hyper_parameter_ranges: Optional[pulumi.Input['SolutionConfigHpoConfigPropertiesAlgorithmHyperParameterRangesPropertiesArgs']] = None,
                 hpo_objective: Optional[pulumi.Input['SolutionConfigHpoConfigPropertiesHpoObjectivePropertiesArgs']] = None,
                 hpo_resource_config: Optional[pulumi.Input['SolutionConfigHpoConfigPropertiesHpoResourceConfigPropertiesArgs']] = None):
        """
        Describes the properties for hyperparameter optimization (HPO)
        :param pulumi.Input['SolutionConfigHpoConfigPropertiesAlgorithmHyperParameterRangesPropertiesArgs'] algorithm_hyper_parameter_ranges: The hyperparameters and their allowable ranges
        :param pulumi.Input['SolutionConfigHpoConfigPropertiesHpoObjectivePropertiesArgs'] hpo_objective: The metric to optimize during HPO.
        :param pulumi.Input['SolutionConfigHpoConfigPropertiesHpoResourceConfigPropertiesArgs'] hpo_resource_config: Describes the resource configuration for hyperparameter optimization (HPO).
        """
        if algorithm_hyper_parameter_ranges is not None:
            pulumi.set(__self__, "algorithm_hyper_parameter_ranges", algorithm_hyper_parameter_ranges)
        if hpo_objective is not None:
            pulumi.set(__self__, "hpo_objective", hpo_objective)
        if hpo_resource_config is not None:
            pulumi.set(__self__, "hpo_resource_config", hpo_resource_config)

    @property
    @pulumi.getter(name="algorithmHyperParameterRanges")
    def algorithm_hyper_parameter_ranges(self) -> Optional[pulumi.Input['SolutionConfigHpoConfigPropertiesAlgorithmHyperParameterRangesPropertiesArgs']]:
        """
        The hyperparameters and their allowable ranges
        """
        return pulumi.get(self, "algorithm_hyper_parameter_ranges")

    @algorithm_hyper_parameter_ranges.setter
    def algorithm_hyper_parameter_ranges(self, value: Optional[pulumi.Input['SolutionConfigHpoConfigPropertiesAlgorithmHyperParameterRangesPropertiesArgs']]):
        pulumi.set(self, "algorithm_hyper_parameter_ranges", value)

    @property
    @pulumi.getter(name="hpoObjective")
    def hpo_objective(self) -> Optional[pulumi.Input['SolutionConfigHpoConfigPropertiesHpoObjectivePropertiesArgs']]:
        """
        The metric to optimize during HPO.
        """
        return pulumi.get(self, "hpo_objective")

    @hpo_objective.setter
    def hpo_objective(self, value: Optional[pulumi.Input['SolutionConfigHpoConfigPropertiesHpoObjectivePropertiesArgs']]):
        pulumi.set(self, "hpo_objective", value)

    @property
    @pulumi.getter(name="hpoResourceConfig")
    def hpo_resource_config(self) -> Optional[pulumi.Input['SolutionConfigHpoConfigPropertiesHpoResourceConfigPropertiesArgs']]:
        """
        Describes the resource configuration for hyperparameter optimization (HPO).
        """
        return pulumi.get(self, "hpo_resource_config")

    @hpo_resource_config.setter
    def hpo_resource_config(self, value: Optional[pulumi.Input['SolutionConfigHpoConfigPropertiesHpoResourceConfigPropertiesArgs']]):
        pulumi.set(self, "hpo_resource_config", value)


@pulumi.input_type
class SolutionConfigArgs:
    def __init__(__self__, *,
                 algorithm_hyper_parameters: Optional[Any] = None,
                 auto_ml_config: Optional[pulumi.Input['SolutionConfigAutoMLConfigPropertiesArgs']] = None,
                 event_value_threshold: Optional[pulumi.Input[str]] = None,
                 feature_transformation_parameters: Optional[Any] = None,
                 hpo_config: Optional[pulumi.Input['SolutionConfigHpoConfigPropertiesArgs']] = None):
        """
        The configuration to use with the solution. When performAutoML is set to true, Amazon Personalize only evaluates the autoMLConfig section of the solution configuration.
        :param Any algorithm_hyper_parameters: Lists the hyperparameter names and ranges.
        :param pulumi.Input['SolutionConfigAutoMLConfigPropertiesArgs'] auto_ml_config: The AutoMLConfig object containing a list of recipes to search when AutoML is performed.
        :param pulumi.Input[str] event_value_threshold: Only events with a value greater than or equal to this threshold are used for training a model.
        :param Any feature_transformation_parameters: Lists the feature transformation parameters.
        :param pulumi.Input['SolutionConfigHpoConfigPropertiesArgs'] hpo_config: Describes the properties for hyperparameter optimization (HPO)
        """
        if algorithm_hyper_parameters is not None:
            pulumi.set(__self__, "algorithm_hyper_parameters", algorithm_hyper_parameters)
        if auto_ml_config is not None:
            pulumi.set(__self__, "auto_ml_config", auto_ml_config)
        if event_value_threshold is not None:
            pulumi.set(__self__, "event_value_threshold", event_value_threshold)
        if feature_transformation_parameters is not None:
            pulumi.set(__self__, "feature_transformation_parameters", feature_transformation_parameters)
        if hpo_config is not None:
            pulumi.set(__self__, "hpo_config", hpo_config)

    @property
    @pulumi.getter(name="algorithmHyperParameters")
    def algorithm_hyper_parameters(self) -> Optional[Any]:
        """
        Lists the hyperparameter names and ranges.
        """
        return pulumi.get(self, "algorithm_hyper_parameters")

    @algorithm_hyper_parameters.setter
    def algorithm_hyper_parameters(self, value: Optional[Any]):
        pulumi.set(self, "algorithm_hyper_parameters", value)

    @property
    @pulumi.getter(name="autoMLConfig")
    def auto_ml_config(self) -> Optional[pulumi.Input['SolutionConfigAutoMLConfigPropertiesArgs']]:
        """
        The AutoMLConfig object containing a list of recipes to search when AutoML is performed.
        """
        return pulumi.get(self, "auto_ml_config")

    @auto_ml_config.setter
    def auto_ml_config(self, value: Optional[pulumi.Input['SolutionConfigAutoMLConfigPropertiesArgs']]):
        pulumi.set(self, "auto_ml_config", value)

    @property
    @pulumi.getter(name="eventValueThreshold")
    def event_value_threshold(self) -> Optional[pulumi.Input[str]]:
        """
        Only events with a value greater than or equal to this threshold are used for training a model.
        """
        return pulumi.get(self, "event_value_threshold")

    @event_value_threshold.setter
    def event_value_threshold(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "event_value_threshold", value)

    @property
    @pulumi.getter(name="featureTransformationParameters")
    def feature_transformation_parameters(self) -> Optional[Any]:
        """
        Lists the feature transformation parameters.
        """
        return pulumi.get(self, "feature_transformation_parameters")

    @feature_transformation_parameters.setter
    def feature_transformation_parameters(self, value: Optional[Any]):
        pulumi.set(self, "feature_transformation_parameters", value)

    @property
    @pulumi.getter(name="hpoConfig")
    def hpo_config(self) -> Optional[pulumi.Input['SolutionConfigHpoConfigPropertiesArgs']]:
        """
        Describes the properties for hyperparameter optimization (HPO)
        """
        return pulumi.get(self, "hpo_config")

    @hpo_config.setter
    def hpo_config(self, value: Optional[pulumi.Input['SolutionConfigHpoConfigPropertiesArgs']]):
        pulumi.set(self, "hpo_config", value)


@pulumi.input_type
class SolutionContinuousHyperParameterRangeArgs:
    def __init__(__self__, *,
                 max_value: Optional[pulumi.Input[float]] = None,
                 min_value: Optional[pulumi.Input[float]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Provides the name and range of a continuous hyperparameter.
        :param pulumi.Input[float] max_value: The maximum allowable value for the hyperparameter.
        :param pulumi.Input[float] min_value: The minimum allowable value for the hyperparameter.
        :param pulumi.Input[str] name: The name of the hyperparameter.
        """
        if max_value is not None:
            pulumi.set(__self__, "max_value", max_value)
        if min_value is not None:
            pulumi.set(__self__, "min_value", min_value)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="maxValue")
    def max_value(self) -> Optional[pulumi.Input[float]]:
        """
        The maximum allowable value for the hyperparameter.
        """
        return pulumi.get(self, "max_value")

    @max_value.setter
    def max_value(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "max_value", value)

    @property
    @pulumi.getter(name="minValue")
    def min_value(self) -> Optional[pulumi.Input[float]]:
        """
        The minimum allowable value for the hyperparameter.
        """
        return pulumi.get(self, "min_value")

    @min_value.setter
    def min_value(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "min_value", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the hyperparameter.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class SolutionIntegerHyperParameterRangeArgs:
    def __init__(__self__, *,
                 max_value: Optional[pulumi.Input[int]] = None,
                 min_value: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Provides the name and range of an integer-valued hyperparameter.
        :param pulumi.Input[int] max_value: The maximum allowable value for the hyperparameter.
        :param pulumi.Input[int] min_value: The minimum allowable value for the hyperparameter.
        :param pulumi.Input[str] name: The name of the hyperparameter.
        """
        if max_value is not None:
            pulumi.set(__self__, "max_value", max_value)
        if min_value is not None:
            pulumi.set(__self__, "min_value", min_value)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="maxValue")
    def max_value(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum allowable value for the hyperparameter.
        """
        return pulumi.get(self, "max_value")

    @max_value.setter
    def max_value(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_value", value)

    @property
    @pulumi.getter(name="minValue")
    def min_value(self) -> Optional[pulumi.Input[int]]:
        """
        The minimum allowable value for the hyperparameter.
        """
        return pulumi.get(self, "min_value")

    @min_value.setter
    def min_value(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "min_value", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the hyperparameter.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


