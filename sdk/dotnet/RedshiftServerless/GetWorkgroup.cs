// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.RedshiftServerless
{
    public static class GetWorkgroup
    {
        /// <summary>
        /// Definition of AWS::RedshiftServerless::Workgroup Resource Type
        /// </summary>
        public static Task<GetWorkgroupResult> InvokeAsync(GetWorkgroupArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetWorkgroupResult>("aws-native:redshiftserverless:getWorkgroup", args ?? new GetWorkgroupArgs(), options.WithDefaults());

        /// <summary>
        /// Definition of AWS::RedshiftServerless::Workgroup Resource Type
        /// </summary>
        public static Output<GetWorkgroupResult> Invoke(GetWorkgroupInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetWorkgroupResult>("aws-native:redshiftserverless:getWorkgroup", args ?? new GetWorkgroupInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetWorkgroupArgs : global::Pulumi.InvokeArgs
    {
        [Input("workgroupName", required: true)]
        public string WorkgroupName { get; set; } = null!;

        public GetWorkgroupArgs()
        {
        }
        public static new GetWorkgroupArgs Empty => new GetWorkgroupArgs();
    }

    public sealed class GetWorkgroupInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("workgroupName", required: true)]
        public Input<string> WorkgroupName { get; set; } = null!;

        public GetWorkgroupInvokeArgs()
        {
        }
        public static new GetWorkgroupInvokeArgs Empty => new GetWorkgroupInvokeArgs();
    }


    [OutputType]
    public sealed class GetWorkgroupResult
    {
        public readonly bool? EnhancedVpcRouting;
        public readonly int? Port;
        public readonly bool? PubliclyAccessible;
        public readonly Outputs.Workgroup? WorkgroupValue;

        [OutputConstructor]
        private GetWorkgroupResult(
            bool? enhancedVpcRouting,

            int? port,

            bool? publiclyAccessible,

            Outputs.Workgroup? workgroup)
        {
            EnhancedVpcRouting = enhancedVpcRouting;
            Port = port;
            PubliclyAccessible = publiclyAccessible;
            WorkgroupValue = workgroup;
        }
    }
}
