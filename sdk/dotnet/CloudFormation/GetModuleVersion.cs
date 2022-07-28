// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CloudFormation
{
    public static class GetModuleVersion
    {
        /// <summary>
        /// A module that has been registered in the CloudFormation registry.
        /// </summary>
        public static Task<GetModuleVersionResult> InvokeAsync(GetModuleVersionArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetModuleVersionResult>("aws-native:cloudformation:getModuleVersion", args ?? new GetModuleVersionArgs(), options.WithDefaults());

        /// <summary>
        /// A module that has been registered in the CloudFormation registry.
        /// </summary>
        public static Output<GetModuleVersionResult> Invoke(GetModuleVersionInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetModuleVersionResult>("aws-native:cloudformation:getModuleVersion", args ?? new GetModuleVersionInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetModuleVersionArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the module.
        /// </summary>
        [Input("arn", required: true)]
        public string Arn { get; set; } = null!;

        public GetModuleVersionArgs()
        {
        }
        public static new GetModuleVersionArgs Empty => new GetModuleVersionArgs();
    }

    public sealed class GetModuleVersionInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the module.
        /// </summary>
        [Input("arn", required: true)]
        public Input<string> Arn { get; set; } = null!;

        public GetModuleVersionInvokeArgs()
        {
        }
        public static new GetModuleVersionInvokeArgs Empty => new GetModuleVersionInvokeArgs();
    }


    [OutputType]
    public sealed class GetModuleVersionResult
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the module.
        /// </summary>
        public readonly string? Arn;
        /// <summary>
        /// The description of the registered module.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// The URL of a page providing detailed documentation for this module.
        /// </summary>
        public readonly string? DocumentationUrl;
        /// <summary>
        /// Indicator of whether this module version is the current default version
        /// </summary>
        public readonly bool? IsDefaultVersion;
        /// <summary>
        /// The schema defining input parameters to and resources generated by the module.
        /// </summary>
        public readonly string? Schema;
        /// <summary>
        /// The time that the specified module version was registered.
        /// </summary>
        public readonly string? TimeCreated;
        /// <summary>
        /// The version ID of the module represented by this module instance.
        /// </summary>
        public readonly string? VersionId;
        /// <summary>
        /// The scope at which the type is visible and usable in CloudFormation operations.
        /// 
        /// The only allowed value at present is:
        /// 
        /// PRIVATE: The type is only visible and usable within the account in which it is registered. Currently, AWS CloudFormation marks any types you register as PRIVATE.
        /// </summary>
        public readonly Pulumi.AwsNative.CloudFormation.ModuleVersionVisibility? Visibility;

        [OutputConstructor]
        private GetModuleVersionResult(
            string? arn,

            string? description,

            string? documentationUrl,

            bool? isDefaultVersion,

            string? schema,

            string? timeCreated,

            string? versionId,

            Pulumi.AwsNative.CloudFormation.ModuleVersionVisibility? visibility)
        {
            Arn = arn;
            Description = description;
            DocumentationUrl = documentationUrl;
            IsDefaultVersion = isDefaultVersion;
            Schema = schema;
            TimeCreated = timeCreated;
            VersionId = versionId;
            Visibility = visibility;
        }
    }
}
