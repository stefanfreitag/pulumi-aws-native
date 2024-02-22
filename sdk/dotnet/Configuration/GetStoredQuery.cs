// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Configuration
{
    public static class GetStoredQuery
    {
        /// <summary>
        /// Resource Type definition for AWS::Config::StoredQuery
        /// </summary>
        public static Task<GetStoredQueryResult> InvokeAsync(GetStoredQueryArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetStoredQueryResult>("aws-native:configuration:getStoredQuery", args ?? new GetStoredQueryArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::Config::StoredQuery
        /// </summary>
        public static Output<GetStoredQueryResult> Invoke(GetStoredQueryInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetStoredQueryResult>("aws-native:configuration:getStoredQuery", args ?? new GetStoredQueryInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetStoredQueryArgs : global::Pulumi.InvokeArgs
    {
        [Input("queryName", required: true)]
        public string QueryName { get; set; } = null!;

        public GetStoredQueryArgs()
        {
        }
        public static new GetStoredQueryArgs Empty => new GetStoredQueryArgs();
    }

    public sealed class GetStoredQueryInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("queryName", required: true)]
        public Input<string> QueryName { get; set; } = null!;

        public GetStoredQueryInvokeArgs()
        {
        }
        public static new GetStoredQueryInvokeArgs Empty => new GetStoredQueryInvokeArgs();
    }


    [OutputType]
    public sealed class GetStoredQueryResult
    {
        public readonly string? QueryArn;
        public readonly string? QueryDescription;
        public readonly string? QueryExpression;
        public readonly string? QueryId;
        /// <summary>
        /// The tags for the stored query.
        /// </summary>
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;

        [OutputConstructor]
        private GetStoredQueryResult(
            string? queryArn,

            string? queryDescription,

            string? queryExpression,

            string? queryId,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags)
        {
            QueryArn = queryArn;
            QueryDescription = queryDescription;
            QueryExpression = queryExpression;
            QueryId = queryId;
            Tags = tags;
        }
    }
}
