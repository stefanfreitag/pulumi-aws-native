// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppSync
{
    /// <summary>
    /// Resource Type definition for AWS::AppSync::DataSource
    /// </summary>
    [Obsolete(@"DataSource is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:appsync:DataSource")]
    public partial class DataSource : global::Pulumi.CustomResource
    {
        [Output("apiId")]
        public Output<string> ApiId { get; private set; } = null!;

        [Output("dataSourceArn")]
        public Output<string> DataSourceArn { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("dynamoDbConfig")]
        public Output<Outputs.DataSourceDynamoDbConfig?> DynamoDbConfig { get; private set; } = null!;

        [Output("elasticsearchConfig")]
        public Output<Outputs.DataSourceElasticsearchConfig?> ElasticsearchConfig { get; private set; } = null!;

        [Output("eventBridgeConfig")]
        public Output<Outputs.DataSourceEventBridgeConfig?> EventBridgeConfig { get; private set; } = null!;

        [Output("httpConfig")]
        public Output<Outputs.DataSourceHttpConfig?> HttpConfig { get; private set; } = null!;

        [Output("lambdaConfig")]
        public Output<Outputs.DataSourceLambdaConfig?> LambdaConfig { get; private set; } = null!;

        [Output("metricsConfig")]
        public Output<string?> MetricsConfig { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("openSearchServiceConfig")]
        public Output<Outputs.DataSourceOpenSearchServiceConfig?> OpenSearchServiceConfig { get; private set; } = null!;

        [Output("relationalDatabaseConfig")]
        public Output<Outputs.DataSourceRelationalDatabaseConfig?> RelationalDatabaseConfig { get; private set; } = null!;

        [Output("serviceRoleArn")]
        public Output<string?> ServiceRoleArn { get; private set; } = null!;

        [Output("type")]
        public Output<string> Type { get; private set; } = null!;


        /// <summary>
        /// Create a DataSource resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public DataSource(string name, DataSourceArgs args, CustomResourceOptions? options = null)
            : base("aws-native:appsync:DataSource", name, args ?? new DataSourceArgs(), MakeResourceOptions(options, ""))
        {
        }

        private DataSource(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:appsync:DataSource", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "apiId",
                    "name",
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
        [Input("apiId", required: true)]
        public Input<string> ApiId { get; set; } = null!;

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("dynamoDbConfig")]
        public Input<Inputs.DataSourceDynamoDbConfigArgs>? DynamoDbConfig { get; set; }

        [Input("elasticsearchConfig")]
        public Input<Inputs.DataSourceElasticsearchConfigArgs>? ElasticsearchConfig { get; set; }

        [Input("eventBridgeConfig")]
        public Input<Inputs.DataSourceEventBridgeConfigArgs>? EventBridgeConfig { get; set; }

        [Input("httpConfig")]
        public Input<Inputs.DataSourceHttpConfigArgs>? HttpConfig { get; set; }

        [Input("lambdaConfig")]
        public Input<Inputs.DataSourceLambdaConfigArgs>? LambdaConfig { get; set; }

        [Input("metricsConfig")]
        public Input<string>? MetricsConfig { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("openSearchServiceConfig")]
        public Input<Inputs.DataSourceOpenSearchServiceConfigArgs>? OpenSearchServiceConfig { get; set; }

        [Input("relationalDatabaseConfig")]
        public Input<Inputs.DataSourceRelationalDatabaseConfigArgs>? RelationalDatabaseConfig { get; set; }

        [Input("serviceRoleArn")]
        public Input<string>? ServiceRoleArn { get; set; }

        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public DataSourceArgs()
        {
        }
        public static new DataSourceArgs Empty => new DataSourceArgs();
    }
}
