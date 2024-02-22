// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight
{
    /// <summary>
    /// Definition of the AWS::QuickSight::DataSet Resource Type.
    /// </summary>
    [AwsNativeResourceType("aws-native:quicksight:DataSet")]
    public partial class DataSet : global::Pulumi.CustomResource
    {
        /// <summary>
        /// &lt;p&gt;The Amazon Resource Name (ARN) of the resource.&lt;/p&gt;
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("awsAccountId")]
        public Output<string?> AwsAccountId { get; private set; } = null!;

        /// <summary>
        /// &lt;p&gt;Groupings of columns that work together in certain QuickSight features. Currently, only geospatial hierarchy is supported.&lt;/p&gt;
        /// </summary>
        [Output("columnGroups")]
        public Output<ImmutableArray<Outputs.DataSetColumnGroup>> ColumnGroups { get; private set; } = null!;

        [Output("columnLevelPermissionRules")]
        public Output<ImmutableArray<Outputs.DataSetColumnLevelPermissionRule>> ColumnLevelPermissionRules { get; private set; } = null!;

        /// <summary>
        /// &lt;p&gt;The amount of SPICE capacity used by this dataset. This is 0 if the dataset isn't
        ///             imported into SPICE.&lt;/p&gt;
        /// </summary>
        [Output("consumedSpiceCapacityInBytes")]
        public Output<double> ConsumedSpiceCapacityInBytes { get; private set; } = null!;

        /// <summary>
        /// &lt;p&gt;The time that this dataset was created.&lt;/p&gt;
        /// </summary>
        [Output("createdTime")]
        public Output<string> CreatedTime { get; private set; } = null!;

        [Output("dataSetId")]
        public Output<string?> DataSetId { get; private set; } = null!;

        [Output("dataSetRefreshProperties")]
        public Output<Outputs.DataSetRefreshProperties?> DataSetRefreshProperties { get; private set; } = null!;

        [Output("dataSetUsageConfiguration")]
        public Output<Outputs.DataSetUsageConfiguration?> DataSetUsageConfiguration { get; private set; } = null!;

        /// <summary>
        /// &lt;p&gt;The parameters declared in the dataset.&lt;/p&gt;
        /// </summary>
        [Output("datasetParameters")]
        public Output<ImmutableArray<Outputs.DataSetDatasetParameter>> DatasetParameters { get; private set; } = null!;

        [Output("fieldFolders")]
        public Output<Outputs.DataSetFieldFolderMap?> FieldFolders { get; private set; } = null!;

        [Output("importMode")]
        public Output<Pulumi.AwsNative.QuickSight.DataSetImportMode?> ImportMode { get; private set; } = null!;

        [Output("ingestionWaitPolicy")]
        public Output<Outputs.DataSetIngestionWaitPolicy?> IngestionWaitPolicy { get; private set; } = null!;

        /// <summary>
        /// &lt;p&gt;The last time that this dataset was updated.&lt;/p&gt;
        /// </summary>
        [Output("lastUpdatedTime")]
        public Output<string> LastUpdatedTime { get; private set; } = null!;

        [Output("logicalTableMap")]
        public Output<Outputs.DataSetLogicalTableMap?> LogicalTableMap { get; private set; } = null!;

        /// <summary>
        /// &lt;p&gt;The display name for the dataset.&lt;/p&gt;
        /// </summary>
        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        /// <summary>
        /// &lt;p&gt;The list of columns after all transforms. These columns are available in templates,
        ///             analyses, and dashboards.&lt;/p&gt;
        /// </summary>
        [Output("outputColumns")]
        public Output<ImmutableArray<Outputs.DataSetOutputColumn>> OutputColumns { get; private set; } = null!;

        /// <summary>
        /// &lt;p&gt;A list of resource permissions on the dataset.&lt;/p&gt;
        /// </summary>
        [Output("permissions")]
        public Output<ImmutableArray<Outputs.DataSetResourcePermission>> Permissions { get; private set; } = null!;

        [Output("physicalTableMap")]
        public Output<Outputs.DataSetPhysicalTableMap?> PhysicalTableMap { get; private set; } = null!;

        [Output("rowLevelPermissionDataSet")]
        public Output<Outputs.DataSetRowLevelPermissionDataSet?> RowLevelPermissionDataSet { get; private set; } = null!;

        [Output("rowLevelPermissionTagConfiguration")]
        public Output<Outputs.DataSetRowLevelPermissionTagConfiguration?> RowLevelPermissionTagConfiguration { get; private set; } = null!;

        /// <summary>
        /// &lt;p&gt;Contains a map of the key-value pairs for the resource tag or tags assigned to the dataset.&lt;/p&gt;
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a DataSet resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public DataSet(string name, DataSetArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:quicksight:DataSet", name, args ?? new DataSetArgs(), MakeResourceOptions(options, ""))
        {
        }

        private DataSet(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:quicksight:DataSet", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "awsAccountId",
                    "dataSetId",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing DataSet resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static DataSet Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new DataSet(name, id, options);
        }
    }

    public sealed class DataSetArgs : global::Pulumi.ResourceArgs
    {
        [Input("awsAccountId")]
        public Input<string>? AwsAccountId { get; set; }

        [Input("columnGroups")]
        private InputList<Inputs.DataSetColumnGroupArgs>? _columnGroups;

        /// <summary>
        /// &lt;p&gt;Groupings of columns that work together in certain QuickSight features. Currently, only geospatial hierarchy is supported.&lt;/p&gt;
        /// </summary>
        public InputList<Inputs.DataSetColumnGroupArgs> ColumnGroups
        {
            get => _columnGroups ?? (_columnGroups = new InputList<Inputs.DataSetColumnGroupArgs>());
            set => _columnGroups = value;
        }

        [Input("columnLevelPermissionRules")]
        private InputList<Inputs.DataSetColumnLevelPermissionRuleArgs>? _columnLevelPermissionRules;
        public InputList<Inputs.DataSetColumnLevelPermissionRuleArgs> ColumnLevelPermissionRules
        {
            get => _columnLevelPermissionRules ?? (_columnLevelPermissionRules = new InputList<Inputs.DataSetColumnLevelPermissionRuleArgs>());
            set => _columnLevelPermissionRules = value;
        }

        [Input("dataSetId")]
        public Input<string>? DataSetId { get; set; }

        [Input("dataSetRefreshProperties")]
        public Input<Inputs.DataSetRefreshPropertiesArgs>? DataSetRefreshProperties { get; set; }

        [Input("dataSetUsageConfiguration")]
        public Input<Inputs.DataSetUsageConfigurationArgs>? DataSetUsageConfiguration { get; set; }

        [Input("datasetParameters")]
        private InputList<Inputs.DataSetDatasetParameterArgs>? _datasetParameters;

        /// <summary>
        /// &lt;p&gt;The parameters declared in the dataset.&lt;/p&gt;
        /// </summary>
        public InputList<Inputs.DataSetDatasetParameterArgs> DatasetParameters
        {
            get => _datasetParameters ?? (_datasetParameters = new InputList<Inputs.DataSetDatasetParameterArgs>());
            set => _datasetParameters = value;
        }

        [Input("fieldFolders")]
        public Input<Inputs.DataSetFieldFolderMapArgs>? FieldFolders { get; set; }

        [Input("importMode")]
        public Input<Pulumi.AwsNative.QuickSight.DataSetImportMode>? ImportMode { get; set; }

        [Input("ingestionWaitPolicy")]
        public Input<Inputs.DataSetIngestionWaitPolicyArgs>? IngestionWaitPolicy { get; set; }

        [Input("logicalTableMap")]
        public Input<Inputs.DataSetLogicalTableMapArgs>? LogicalTableMap { get; set; }

        /// <summary>
        /// &lt;p&gt;The display name for the dataset.&lt;/p&gt;
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("permissions")]
        private InputList<Inputs.DataSetResourcePermissionArgs>? _permissions;

        /// <summary>
        /// &lt;p&gt;A list of resource permissions on the dataset.&lt;/p&gt;
        /// </summary>
        public InputList<Inputs.DataSetResourcePermissionArgs> Permissions
        {
            get => _permissions ?? (_permissions = new InputList<Inputs.DataSetResourcePermissionArgs>());
            set => _permissions = value;
        }

        [Input("physicalTableMap")]
        public Input<Inputs.DataSetPhysicalTableMapArgs>? PhysicalTableMap { get; set; }

        [Input("rowLevelPermissionDataSet")]
        public Input<Inputs.DataSetRowLevelPermissionDataSetArgs>? RowLevelPermissionDataSet { get; set; }

        [Input("rowLevelPermissionTagConfiguration")]
        public Input<Inputs.DataSetRowLevelPermissionTagConfigurationArgs>? RowLevelPermissionTagConfiguration { get; set; }

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;

        /// <summary>
        /// &lt;p&gt;Contains a map of the key-value pairs for the resource tag or tags assigned to the dataset.&lt;/p&gt;
        /// </summary>
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        public DataSetArgs()
        {
        }
        public static new DataSetArgs Empty => new DataSetArgs();
    }
}
