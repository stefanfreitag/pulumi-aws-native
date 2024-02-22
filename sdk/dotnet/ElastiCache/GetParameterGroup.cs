// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ElastiCache
{
    public static class GetParameterGroup
    {
        /// <summary>
        /// Resource Type definition for AWS::ElastiCache::ParameterGroup
        /// </summary>
        public static Task<GetParameterGroupResult> InvokeAsync(GetParameterGroupArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetParameterGroupResult>("aws-native:elasticache:getParameterGroup", args ?? new GetParameterGroupArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::ElastiCache::ParameterGroup
        /// </summary>
        public static Output<GetParameterGroupResult> Invoke(GetParameterGroupInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetParameterGroupResult>("aws-native:elasticache:getParameterGroup", args ?? new GetParameterGroupInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetParameterGroupArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetParameterGroupArgs()
        {
        }
        public static new GetParameterGroupArgs Empty => new GetParameterGroupArgs();
    }

    public sealed class GetParameterGroupInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetParameterGroupInvokeArgs()
        {
        }
        public static new GetParameterGroupInvokeArgs Empty => new GetParameterGroupInvokeArgs();
    }


    [OutputType]
    public sealed class GetParameterGroupResult
    {
        public readonly string? Description;
        public readonly string? Id;
        public readonly ImmutableDictionary<string, string>? Properties;
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;

        [OutputConstructor]
        private GetParameterGroupResult(
            string? description,

            string? id,

            ImmutableDictionary<string, string>? properties,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags)
        {
            Description = description;
            Id = id;
            Properties = properties;
            Tags = tags;
        }
    }
}
