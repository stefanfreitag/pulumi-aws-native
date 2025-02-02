// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppSync
{
    public static class GetDataSource
    {
        /// <summary>
        /// Resource Type definition for AWS::AppSync::DataSource
        /// </summary>
        public static Task<GetDataSourceResult> InvokeAsync(GetDataSourceArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetDataSourceResult>("aws-native:appsync:getDataSource", args ?? new GetDataSourceArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::AppSync::DataSource
        /// </summary>
        public static Output<GetDataSourceResult> Invoke(GetDataSourceInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetDataSourceResult>("aws-native:appsync:getDataSource", args ?? new GetDataSourceInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDataSourceArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetDataSourceArgs()
        {
        }
        public static new GetDataSourceArgs Empty => new GetDataSourceArgs();
    }

    public sealed class GetDataSourceInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetDataSourceInvokeArgs()
        {
        }
        public static new GetDataSourceInvokeArgs Empty => new GetDataSourceInvokeArgs();
    }


    [OutputType]
    public sealed class GetDataSourceResult
    {
        public readonly string? DataSourceArn;
        public readonly string? Description;
        public readonly Outputs.DataSourceDynamoDbConfig? DynamoDbConfig;
        public readonly Outputs.DataSourceElasticsearchConfig? ElasticsearchConfig;
        public readonly Outputs.DataSourceEventBridgeConfig? EventBridgeConfig;
        public readonly Outputs.DataSourceHttpConfig? HttpConfig;
        public readonly string? Id;
        public readonly Outputs.DataSourceLambdaConfig? LambdaConfig;
        public readonly string? MetricsConfig;
        public readonly Outputs.DataSourceOpenSearchServiceConfig? OpenSearchServiceConfig;
        public readonly Outputs.DataSourceRelationalDatabaseConfig? RelationalDatabaseConfig;
        public readonly string? ServiceRoleArn;
        public readonly string? Type;

        [OutputConstructor]
        private GetDataSourceResult(
            string? dataSourceArn,

            string? description,

            Outputs.DataSourceDynamoDbConfig? dynamoDbConfig,

            Outputs.DataSourceElasticsearchConfig? elasticsearchConfig,

            Outputs.DataSourceEventBridgeConfig? eventBridgeConfig,

            Outputs.DataSourceHttpConfig? httpConfig,

            string? id,

            Outputs.DataSourceLambdaConfig? lambdaConfig,

            string? metricsConfig,

            Outputs.DataSourceOpenSearchServiceConfig? openSearchServiceConfig,

            Outputs.DataSourceRelationalDatabaseConfig? relationalDatabaseConfig,

            string? serviceRoleArn,

            string? type)
        {
            DataSourceArn = dataSourceArn;
            Description = description;
            DynamoDbConfig = dynamoDbConfig;
            ElasticsearchConfig = elasticsearchConfig;
            EventBridgeConfig = eventBridgeConfig;
            HttpConfig = httpConfig;
            Id = id;
            LambdaConfig = lambdaConfig;
            MetricsConfig = metricsConfig;
            OpenSearchServiceConfig = openSearchServiceConfig;
            RelationalDatabaseConfig = relationalDatabaseConfig;
            ServiceRoleArn = serviceRoleArn;
            Type = type;
        }
    }
}
