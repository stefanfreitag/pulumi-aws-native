// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2
{
    public static class GetSecurityGroupIngress
    {
        /// <summary>
        /// Resource Type definition for AWS::EC2::SecurityGroupIngress
        /// </summary>
        public static Task<GetSecurityGroupIngressResult> InvokeAsync(GetSecurityGroupIngressArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetSecurityGroupIngressResult>("aws-native:ec2:getSecurityGroupIngress", args ?? new GetSecurityGroupIngressArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::EC2::SecurityGroupIngress
        /// </summary>
        public static Output<GetSecurityGroupIngressResult> Invoke(GetSecurityGroupIngressInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetSecurityGroupIngressResult>("aws-native:ec2:getSecurityGroupIngress", args ?? new GetSecurityGroupIngressInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetSecurityGroupIngressArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetSecurityGroupIngressArgs()
        {
        }
        public static new GetSecurityGroupIngressArgs Empty => new GetSecurityGroupIngressArgs();
    }

    public sealed class GetSecurityGroupIngressInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetSecurityGroupIngressInvokeArgs()
        {
        }
        public static new GetSecurityGroupIngressInvokeArgs Empty => new GetSecurityGroupIngressInvokeArgs();
    }


    [OutputType]
    public sealed class GetSecurityGroupIngressResult
    {
        public readonly string? Description;
        public readonly string? Id;

        [OutputConstructor]
        private GetSecurityGroupIngressResult(
            string? description,

            string? id)
        {
            Description = description;
            Id = id;
        }
    }
}
