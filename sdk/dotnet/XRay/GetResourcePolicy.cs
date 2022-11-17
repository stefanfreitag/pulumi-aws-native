// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.XRay
{
    public static class GetResourcePolicy
    {
        /// <summary>
        /// This schema provides construct and validation rules for AWS-XRay Resource Policy resource parameters.
        /// </summary>
        public static Task<GetResourcePolicyResult> InvokeAsync(GetResourcePolicyArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetResourcePolicyResult>("aws-native:xray:getResourcePolicy", args ?? new GetResourcePolicyArgs(), options.WithDefaults());

        /// <summary>
        /// This schema provides construct and validation rules for AWS-XRay Resource Policy resource parameters.
        /// </summary>
        public static Output<GetResourcePolicyResult> Invoke(GetResourcePolicyInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetResourcePolicyResult>("aws-native:xray:getResourcePolicy", args ?? new GetResourcePolicyInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetResourcePolicyArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the resource policy. Must be unique within a specific AWS account.
        /// </summary>
        [Input("policyName", required: true)]
        public string PolicyName { get; set; } = null!;

        public GetResourcePolicyArgs()
        {
        }
        public static new GetResourcePolicyArgs Empty => new GetResourcePolicyArgs();
    }

    public sealed class GetResourcePolicyInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the resource policy. Must be unique within a specific AWS account.
        /// </summary>
        [Input("policyName", required: true)]
        public Input<string> PolicyName { get; set; } = null!;

        public GetResourcePolicyInvokeArgs()
        {
        }
        public static new GetResourcePolicyInvokeArgs Empty => new GetResourcePolicyInvokeArgs();
    }


    [OutputType]
    public sealed class GetResourcePolicyResult
    {
        /// <summary>
        /// The resource policy document, which can be up to 5kb in size.
        /// </summary>
        public readonly string? PolicyDocument;

        [OutputConstructor]
        private GetResourcePolicyResult(string? policyDocument)
        {
            PolicyDocument = policyDocument;
        }
    }
}
