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
    /// Definition of the AWS::QuickSight::DataSource Resource Type.
    /// </summary>
    [AwsNativeResourceType("aws-native:quicksight:DataSource")]
    public partial class DataSource : global::Pulumi.CustomResource
    {
        /// <summary>
        /// &lt;p&gt;A set of alternate data source parameters that you want to share for the credentials
        ///             stored with this data source. The credentials are applied in tandem with the data source
        ///             parameters when you copy a data source by using a create or update request. The API
        ///             operation compares the &lt;code&gt;DataSourceParameters&lt;/code&gt; structure that's in the request
        ///             with the structures in the &lt;code&gt;AlternateDataSourceParameters&lt;/code&gt; allow list. If the
        ///             structures are an exact match, the request is allowed to use the credentials from this
        ///             existing data source. If the &lt;code&gt;AlternateDataSourceParameters&lt;/code&gt; list is null,
        ///             the &lt;code&gt;Credentials&lt;/code&gt; originally used with this &lt;code&gt;DataSourceParameters&lt;/code&gt;
        ///             are automatically allowed.&lt;/p&gt;
        /// </summary>
        [Output("alternateDataSourceParameters")]
        public Output<ImmutableArray<Outputs.DataSourceParameters>> AlternateDataSourceParameters { get; private set; } = null!;

        /// <summary>
        /// &lt;p&gt;The Amazon Resource Name (ARN) of the data source.&lt;/p&gt;
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("awsAccountId")]
        public Output<string?> AwsAccountId { get; private set; } = null!;

        /// <summary>
        /// &lt;p&gt;The time that this data source was created.&lt;/p&gt;
        /// </summary>
        [Output("createdTime")]
        public Output<string> CreatedTime { get; private set; } = null!;

        [Output("credentials")]
        public Output<Outputs.DataSourceCredentials?> Credentials { get; private set; } = null!;

        [Output("dataSourceId")]
        public Output<string?> DataSourceId { get; private set; } = null!;

        [Output("dataSourceParameters")]
        public Output<Outputs.DataSourceParameters?> DataSourceParameters { get; private set; } = null!;

        [Output("errorInfo")]
        public Output<Outputs.DataSourceErrorInfo?> ErrorInfo { get; private set; } = null!;

        /// <summary>
        /// &lt;p&gt;The last time that this data source was updated.&lt;/p&gt;
        /// </summary>
        [Output("lastUpdatedTime")]
        public Output<string> LastUpdatedTime { get; private set; } = null!;

        /// <summary>
        /// &lt;p&gt;A display name for the data source.&lt;/p&gt;
        /// </summary>
        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        /// <summary>
        /// &lt;p&gt;A list of resource permissions on the data source.&lt;/p&gt;
        /// </summary>
        [Output("permissions")]
        public Output<ImmutableArray<Outputs.DataSourceResourcePermission>> Permissions { get; private set; } = null!;

        [Output("sslProperties")]
        public Output<Outputs.DataSourceSslProperties?> SslProperties { get; private set; } = null!;

        [Output("status")]
        public Output<Pulumi.AwsNative.QuickSight.DataSourceResourceStatus> Status { get; private set; } = null!;

        /// <summary>
        /// &lt;p&gt;Contains a map of the key-value pairs for the resource tag or tags assigned to the data source.&lt;/p&gt;
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;

        [Output("type")]
        public Output<Pulumi.AwsNative.QuickSight.DataSourceType?> Type { get; private set; } = null!;

        [Output("vpcConnectionProperties")]
        public Output<Outputs.DataSourceVpcConnectionProperties?> VpcConnectionProperties { get; private set; } = null!;


        /// <summary>
        /// Create a DataSource resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public DataSource(string name, DataSourceArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:quicksight:DataSource", name, args ?? new DataSourceArgs(), MakeResourceOptions(options, ""))
        {
        }

        private DataSource(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:quicksight:DataSource", name, null, MakeResourceOptions(options, id))
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
                    "dataSourceId",
                    "type",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing DataSource resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static DataSource Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new DataSource(name, id, options);
        }
    }

    public sealed class DataSourceArgs : global::Pulumi.ResourceArgs
    {
        [Input("alternateDataSourceParameters")]
        private InputList<Inputs.DataSourceParametersArgs>? _alternateDataSourceParameters;

        /// <summary>
        /// &lt;p&gt;A set of alternate data source parameters that you want to share for the credentials
        ///             stored with this data source. The credentials are applied in tandem with the data source
        ///             parameters when you copy a data source by using a create or update request. The API
        ///             operation compares the &lt;code&gt;DataSourceParameters&lt;/code&gt; structure that's in the request
        ///             with the structures in the &lt;code&gt;AlternateDataSourceParameters&lt;/code&gt; allow list. If the
        ///             structures are an exact match, the request is allowed to use the credentials from this
        ///             existing data source. If the &lt;code&gt;AlternateDataSourceParameters&lt;/code&gt; list is null,
        ///             the &lt;code&gt;Credentials&lt;/code&gt; originally used with this &lt;code&gt;DataSourceParameters&lt;/code&gt;
        ///             are automatically allowed.&lt;/p&gt;
        /// </summary>
        public InputList<Inputs.DataSourceParametersArgs> AlternateDataSourceParameters
        {
            get => _alternateDataSourceParameters ?? (_alternateDataSourceParameters = new InputList<Inputs.DataSourceParametersArgs>());
            set => _alternateDataSourceParameters = value;
        }

        [Input("awsAccountId")]
        public Input<string>? AwsAccountId { get; set; }

        [Input("credentials")]
        public Input<Inputs.DataSourceCredentialsArgs>? Credentials { get; set; }

        [Input("dataSourceId")]
        public Input<string>? DataSourceId { get; set; }

        [Input("dataSourceParameters")]
        public Input<Inputs.DataSourceParametersArgs>? DataSourceParameters { get; set; }

        [Input("errorInfo")]
        public Input<Inputs.DataSourceErrorInfoArgs>? ErrorInfo { get; set; }

        /// <summary>
        /// &lt;p&gt;A display name for the data source.&lt;/p&gt;
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("permissions")]
        private InputList<Inputs.DataSourceResourcePermissionArgs>? _permissions;

        /// <summary>
        /// &lt;p&gt;A list of resource permissions on the data source.&lt;/p&gt;
        /// </summary>
        public InputList<Inputs.DataSourceResourcePermissionArgs> Permissions
        {
            get => _permissions ?? (_permissions = new InputList<Inputs.DataSourceResourcePermissionArgs>());
            set => _permissions = value;
        }

        [Input("sslProperties")]
        public Input<Inputs.DataSourceSslPropertiesArgs>? SslProperties { get; set; }

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;

        /// <summary>
        /// &lt;p&gt;Contains a map of the key-value pairs for the resource tag or tags assigned to the data source.&lt;/p&gt;
        /// </summary>
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        [Input("type")]
        public Input<Pulumi.AwsNative.QuickSight.DataSourceType>? Type { get; set; }

        [Input("vpcConnectionProperties")]
        public Input<Inputs.DataSourceVpcConnectionPropertiesArgs>? VpcConnectionProperties { get; set; }

        public DataSourceArgs()
        {
        }
        public static new DataSourceArgs Empty => new DataSourceArgs();
    }
}
