// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WAF
{
    public static class GetByteMatchSet
    {
        /// <summary>
        /// Resource Type definition for AWS::WAF::ByteMatchSet
        /// </summary>
        public static Task<GetByteMatchSetResult> InvokeAsync(GetByteMatchSetArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetByteMatchSetResult>("aws-native:waf:getByteMatchSet", args ?? new GetByteMatchSetArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::WAF::ByteMatchSet
        /// </summary>
        public static Output<GetByteMatchSetResult> Invoke(GetByteMatchSetInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetByteMatchSetResult>("aws-native:waf:getByteMatchSet", args ?? new GetByteMatchSetInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetByteMatchSetArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetByteMatchSetArgs()
        {
        }
        public static new GetByteMatchSetArgs Empty => new GetByteMatchSetArgs();
    }

    public sealed class GetByteMatchSetInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetByteMatchSetInvokeArgs()
        {
        }
        public static new GetByteMatchSetInvokeArgs Empty => new GetByteMatchSetInvokeArgs();
    }


    [OutputType]
    public sealed class GetByteMatchSetResult
    {
        public readonly ImmutableArray<Outputs.ByteMatchSetByteMatchTuple> ByteMatchTuples;
        public readonly string? Id;

        [OutputConstructor]
        private GetByteMatchSetResult(
            ImmutableArray<Outputs.ByteMatchSetByteMatchTuple> byteMatchTuples,

            string? id)
        {
            ByteMatchTuples = byteMatchTuples;
            Id = id;
        }
    }
}
