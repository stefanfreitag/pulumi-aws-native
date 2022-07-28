// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WAF
{
    public static class GetIPSet
    {
        /// <summary>
        /// Resource Type definition for AWS::WAF::IPSet
        /// </summary>
        public static Task<GetIPSetResult> InvokeAsync(GetIPSetArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetIPSetResult>("aws-native:waf:getIPSet", args ?? new GetIPSetArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::WAF::IPSet
        /// </summary>
        public static Output<GetIPSetResult> Invoke(GetIPSetInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetIPSetResult>("aws-native:waf:getIPSet", args ?? new GetIPSetInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetIPSetArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetIPSetArgs()
        {
        }
        public static new GetIPSetArgs Empty => new GetIPSetArgs();
    }

    public sealed class GetIPSetInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetIPSetInvokeArgs()
        {
        }
        public static new GetIPSetInvokeArgs Empty => new GetIPSetInvokeArgs();
    }


    [OutputType]
    public sealed class GetIPSetResult
    {
        public readonly ImmutableArray<Outputs.IPSetDescriptor> IPSetDescriptors;
        public readonly string? Id;

        [OutputConstructor]
        private GetIPSetResult(
            ImmutableArray<Outputs.IPSetDescriptor> iPSetDescriptors,

            string? id)
        {
            IPSetDescriptors = iPSetDescriptors;
            Id = id;
        }
    }
}
