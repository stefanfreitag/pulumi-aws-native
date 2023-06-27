// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker
{
    public static class GetProject
    {
        /// <summary>
        /// Resource Type definition for AWS::SageMaker::Project
        /// </summary>
        public static Task<GetProjectResult> InvokeAsync(GetProjectArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetProjectResult>("aws-native:sagemaker:getProject", args ?? new GetProjectArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::SageMaker::Project
        /// </summary>
        public static Output<GetProjectResult> Invoke(GetProjectInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetProjectResult>("aws-native:sagemaker:getProject", args ?? new GetProjectInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetProjectArgs : global::Pulumi.InvokeArgs
    {
        [Input("projectArn", required: true)]
        public string ProjectArn { get; set; } = null!;

        public GetProjectArgs()
        {
        }
        public static new GetProjectArgs Empty => new GetProjectArgs();
    }

    public sealed class GetProjectInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("projectArn", required: true)]
        public Input<string> ProjectArn { get; set; } = null!;

        public GetProjectInvokeArgs()
        {
        }
        public static new GetProjectInvokeArgs Empty => new GetProjectInvokeArgs();
    }


    [OutputType]
    public sealed class GetProjectResult
    {
        /// <summary>
        /// The time at which the project was created.
        /// </summary>
        public readonly string? CreationTime;
        public readonly string? ProjectArn;
        public readonly string? ProjectId;
        /// <summary>
        /// The status of a project.
        /// </summary>
        public readonly Pulumi.AwsNative.SageMaker.ProjectStatus? ProjectStatus;
        /// <summary>
        /// Provisioned ServiceCatalog  Details
        /// </summary>
        public readonly Outputs.ServiceCatalogProvisionedProductDetailsProperties? ServiceCatalogProvisionedProductDetails;

        [OutputConstructor]
        private GetProjectResult(
            string? creationTime,

            string? projectArn,

            string? projectId,

            Pulumi.AwsNative.SageMaker.ProjectStatus? projectStatus,

            Outputs.ServiceCatalogProvisionedProductDetailsProperties? serviceCatalogProvisionedProductDetails)
        {
            CreationTime = creationTime;
            ProjectArn = projectArn;
            ProjectId = projectId;
            ProjectStatus = projectStatus;
            ServiceCatalogProvisionedProductDetails = serviceCatalogProvisionedProductDetails;
        }
    }
}
