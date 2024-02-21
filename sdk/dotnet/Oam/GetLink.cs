// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Oam
{
    public static class GetLink
    {
        /// <summary>
        /// Definition of AWS::Oam::Link Resource Type
        /// </summary>
        public static Task<GetLinkResult> InvokeAsync(GetLinkArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetLinkResult>("aws-native:oam:getLink", args ?? new GetLinkArgs(), options.WithDefaults());

        /// <summary>
        /// Definition of AWS::Oam::Link Resource Type
        /// </summary>
        public static Output<GetLinkResult> Invoke(GetLinkInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetLinkResult>("aws-native:oam:getLink", args ?? new GetLinkInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetLinkArgs : global::Pulumi.InvokeArgs
    {
        [Input("arn", required: true)]
        public string Arn { get; set; } = null!;

        public GetLinkArgs()
        {
        }
        public static new GetLinkArgs Empty => new GetLinkArgs();
    }

    public sealed class GetLinkInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("arn", required: true)]
        public Input<string> Arn { get; set; } = null!;

        public GetLinkInvokeArgs()
        {
        }
        public static new GetLinkInvokeArgs Empty => new GetLinkInvokeArgs();
    }


    [OutputType]
    public sealed class GetLinkResult
    {
        public readonly string? Arn;
        public readonly string? Label;
        public readonly ImmutableArray<Pulumi.AwsNative.Oam.LinkResourceType> ResourceTypes;
        /// <summary>
        /// Tags to apply to the link
        /// 
        /// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Oam::Link` for more information about the expected schema for this property.
        /// </summary>
        public readonly object? Tags;

        [OutputConstructor]
        private GetLinkResult(
            string? arn,

            string? label,

            ImmutableArray<Pulumi.AwsNative.Oam.LinkResourceType> resourceTypes,

            object? tags)
        {
            Arn = arn;
            Label = label;
            ResourceTypes = resourceTypes;
            Tags = tags;
        }
    }
}
