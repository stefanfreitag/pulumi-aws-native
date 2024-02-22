// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppIntegrations
{
    public static class GetDataIntegration
    {
        /// <summary>
        /// Resource Type definition for AWS::AppIntegrations::DataIntegration
        /// </summary>
        public static Task<GetDataIntegrationResult> InvokeAsync(GetDataIntegrationArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetDataIntegrationResult>("aws-native:appintegrations:getDataIntegration", args ?? new GetDataIntegrationArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::AppIntegrations::DataIntegration
        /// </summary>
        public static Output<GetDataIntegrationResult> Invoke(GetDataIntegrationInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetDataIntegrationResult>("aws-native:appintegrations:getDataIntegration", args ?? new GetDataIntegrationInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDataIntegrationArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The unique identifer of the data integration.
        /// </summary>
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetDataIntegrationArgs()
        {
        }
        public static new GetDataIntegrationArgs Empty => new GetDataIntegrationArgs();
    }

    public sealed class GetDataIntegrationInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The unique identifer of the data integration.
        /// </summary>
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetDataIntegrationInvokeArgs()
        {
        }
        public static new GetDataIntegrationInvokeArgs Empty => new GetDataIntegrationInvokeArgs();
    }


    [OutputType]
    public sealed class GetDataIntegrationResult
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the data integration.
        /// </summary>
        public readonly string? DataIntegrationArn;
        /// <summary>
        /// The data integration description.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// The configuration for what files should be pulled from the source.
        /// </summary>
        public readonly Outputs.DataIntegrationFileConfiguration? FileConfiguration;
        /// <summary>
        /// The unique identifer of the data integration.
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// The name of the data integration.
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// The configuration for what data should be pulled from the source.
        /// </summary>
        public readonly Outputs.DataIntegrationObjectConfiguration? ObjectConfiguration;
        /// <summary>
        /// The tags (keys and values) associated with the data integration.
        /// </summary>
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;

        [OutputConstructor]
        private GetDataIntegrationResult(
            string? dataIntegrationArn,

            string? description,

            Outputs.DataIntegrationFileConfiguration? fileConfiguration,

            string? id,

            string? name,

            Outputs.DataIntegrationObjectConfiguration? objectConfiguration,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags)
        {
            DataIntegrationArn = dataIntegrationArn;
            Description = description;
            FileConfiguration = fileConfiguration;
            Id = id;
            Name = name;
            ObjectConfiguration = objectConfiguration;
            Tags = tags;
        }
    }
}
