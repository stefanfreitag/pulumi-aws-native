// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoT
{
    public static class GetPolicyPrincipalAttachment
    {
        /// <summary>
        /// Resource Type definition for AWS::IoT::PolicyPrincipalAttachment
        /// </summary>
        public static Task<GetPolicyPrincipalAttachmentResult> InvokeAsync(GetPolicyPrincipalAttachmentArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetPolicyPrincipalAttachmentResult>("aws-native:iot:getPolicyPrincipalAttachment", args ?? new GetPolicyPrincipalAttachmentArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::IoT::PolicyPrincipalAttachment
        /// </summary>
        public static Output<GetPolicyPrincipalAttachmentResult> Invoke(GetPolicyPrincipalAttachmentInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetPolicyPrincipalAttachmentResult>("aws-native:iot:getPolicyPrincipalAttachment", args ?? new GetPolicyPrincipalAttachmentInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPolicyPrincipalAttachmentArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetPolicyPrincipalAttachmentArgs()
        {
        }
        public static new GetPolicyPrincipalAttachmentArgs Empty => new GetPolicyPrincipalAttachmentArgs();
    }

    public sealed class GetPolicyPrincipalAttachmentInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetPolicyPrincipalAttachmentInvokeArgs()
        {
        }
        public static new GetPolicyPrincipalAttachmentInvokeArgs Empty => new GetPolicyPrincipalAttachmentInvokeArgs();
    }


    [OutputType]
    public sealed class GetPolicyPrincipalAttachmentResult
    {
        public readonly string? Id;

        [OutputConstructor]
        private GetPolicyPrincipalAttachmentResult(string? id)
        {
            Id = id;
        }
    }
}
