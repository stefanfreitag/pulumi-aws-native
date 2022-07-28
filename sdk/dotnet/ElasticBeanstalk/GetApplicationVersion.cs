// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ElasticBeanstalk
{
    public static class GetApplicationVersion
    {
        /// <summary>
        /// Resource Type definition for AWS::ElasticBeanstalk::ApplicationVersion
        /// </summary>
        public static Task<GetApplicationVersionResult> InvokeAsync(GetApplicationVersionArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetApplicationVersionResult>("aws-native:elasticbeanstalk:getApplicationVersion", args ?? new GetApplicationVersionArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::ElasticBeanstalk::ApplicationVersion
        /// </summary>
        public static Output<GetApplicationVersionResult> Invoke(GetApplicationVersionInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetApplicationVersionResult>("aws-native:elasticbeanstalk:getApplicationVersion", args ?? new GetApplicationVersionInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetApplicationVersionArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetApplicationVersionArgs()
        {
        }
        public static new GetApplicationVersionArgs Empty => new GetApplicationVersionArgs();
    }

    public sealed class GetApplicationVersionInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetApplicationVersionInvokeArgs()
        {
        }
        public static new GetApplicationVersionInvokeArgs Empty => new GetApplicationVersionInvokeArgs();
    }


    [OutputType]
    public sealed class GetApplicationVersionResult
    {
        public readonly string? Description;
        public readonly string? Id;

        [OutputConstructor]
        private GetApplicationVersionResult(
            string? description,

            string? id)
        {
            Description = description;
            Id = id;
        }
    }
}
