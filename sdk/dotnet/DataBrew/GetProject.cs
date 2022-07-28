// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DataBrew
{
    public static class GetProject
    {
        /// <summary>
        /// Resource schema for AWS::DataBrew::Project.
        /// </summary>
        public static Task<GetProjectResult> InvokeAsync(GetProjectArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetProjectResult>("aws-native:databrew:getProject", args ?? new GetProjectArgs(), options.WithDefaults());

        /// <summary>
        /// Resource schema for AWS::DataBrew::Project.
        /// </summary>
        public static Output<GetProjectResult> Invoke(GetProjectInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetProjectResult>("aws-native:databrew:getProject", args ?? new GetProjectInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetProjectArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Project name
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetProjectArgs()
        {
        }
        public static new GetProjectArgs Empty => new GetProjectArgs();
    }

    public sealed class GetProjectInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Project name
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetProjectInvokeArgs()
        {
        }
        public static new GetProjectInvokeArgs Empty => new GetProjectInvokeArgs();
    }


    [OutputType]
    public sealed class GetProjectResult
    {
        /// <summary>
        /// Dataset name
        /// </summary>
        public readonly string? DatasetName;
        /// <summary>
        /// Recipe name
        /// </summary>
        public readonly string? RecipeName;
        /// <summary>
        /// Role arn
        /// </summary>
        public readonly string? RoleArn;
        /// <summary>
        /// Sample
        /// </summary>
        public readonly Outputs.ProjectSample? Sample;

        [OutputConstructor]
        private GetProjectResult(
            string? datasetName,

            string? recipeName,

            string? roleArn,

            Outputs.ProjectSample? sample)
        {
            DatasetName = datasetName;
            RecipeName = recipeName;
            RoleArn = roleArn;
            Sample = sample;
        }
    }
}
