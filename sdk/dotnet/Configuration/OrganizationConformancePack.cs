// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Configuration
{
    /// <summary>
    /// Resource schema for AWS::Config::OrganizationConformancePack.
    /// </summary>
    [AwsNativeResourceType("aws-native:configuration:OrganizationConformancePack")]
    public partial class OrganizationConformancePack : global::Pulumi.CustomResource
    {
        /// <summary>
        /// A list of ConformancePackInputParameter objects.
        /// </summary>
        [Output("conformancePackInputParameters")]
        public Output<ImmutableArray<Outputs.OrganizationConformancePackConformancePackInputParameter>> ConformancePackInputParameters { get; private set; } = null!;

        /// <summary>
        /// AWS Config stores intermediate files while processing conformance pack template.
        /// </summary>
        [Output("deliveryS3Bucket")]
        public Output<string?> DeliveryS3Bucket { get; private set; } = null!;

        /// <summary>
        /// The prefix for the delivery S3 bucket.
        /// </summary>
        [Output("deliveryS3KeyPrefix")]
        public Output<string?> DeliveryS3KeyPrefix { get; private set; } = null!;

        /// <summary>
        /// A list of AWS accounts to be excluded from an organization conformance pack while deploying a conformance pack.
        /// </summary>
        [Output("excludedAccounts")]
        public Output<ImmutableArray<string>> ExcludedAccounts { get; private set; } = null!;

        /// <summary>
        /// The name of the organization conformance pack.
        /// </summary>
        [Output("organizationConformancePackName")]
        public Output<string> OrganizationConformancePackName { get; private set; } = null!;

        /// <summary>
        /// A string containing full conformance pack template body.
        /// </summary>
        [Output("templateBody")]
        public Output<string?> TemplateBody { get; private set; } = null!;

        /// <summary>
        /// Location of file containing the template body.
        /// </summary>
        [Output("templateS3Uri")]
        public Output<string?> TemplateS3Uri { get; private set; } = null!;


        /// <summary>
        /// Create a OrganizationConformancePack resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public OrganizationConformancePack(string name, OrganizationConformancePackArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:configuration:OrganizationConformancePack", name, args ?? new OrganizationConformancePackArgs(), MakeResourceOptions(options, ""))
        {
        }

        private OrganizationConformancePack(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:configuration:OrganizationConformancePack", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing OrganizationConformancePack resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static OrganizationConformancePack Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new OrganizationConformancePack(name, id, options);
        }
    }

    public sealed class OrganizationConformancePackArgs : global::Pulumi.ResourceArgs
    {
        [Input("conformancePackInputParameters")]
        private InputList<Inputs.OrganizationConformancePackConformancePackInputParameterArgs>? _conformancePackInputParameters;

        /// <summary>
        /// A list of ConformancePackInputParameter objects.
        /// </summary>
        public InputList<Inputs.OrganizationConformancePackConformancePackInputParameterArgs> ConformancePackInputParameters
        {
            get => _conformancePackInputParameters ?? (_conformancePackInputParameters = new InputList<Inputs.OrganizationConformancePackConformancePackInputParameterArgs>());
            set => _conformancePackInputParameters = value;
        }

        /// <summary>
        /// AWS Config stores intermediate files while processing conformance pack template.
        /// </summary>
        [Input("deliveryS3Bucket")]
        public Input<string>? DeliveryS3Bucket { get; set; }

        /// <summary>
        /// The prefix for the delivery S3 bucket.
        /// </summary>
        [Input("deliveryS3KeyPrefix")]
        public Input<string>? DeliveryS3KeyPrefix { get; set; }

        [Input("excludedAccounts")]
        private InputList<string>? _excludedAccounts;

        /// <summary>
        /// A list of AWS accounts to be excluded from an organization conformance pack while deploying a conformance pack.
        /// </summary>
        public InputList<string> ExcludedAccounts
        {
            get => _excludedAccounts ?? (_excludedAccounts = new InputList<string>());
            set => _excludedAccounts = value;
        }

        /// <summary>
        /// The name of the organization conformance pack.
        /// </summary>
        [Input("organizationConformancePackName")]
        public Input<string>? OrganizationConformancePackName { get; set; }

        /// <summary>
        /// A string containing full conformance pack template body.
        /// </summary>
        [Input("templateBody")]
        public Input<string>? TemplateBody { get; set; }

        /// <summary>
        /// Location of file containing the template body.
        /// </summary>
        [Input("templateS3Uri")]
        public Input<string>? TemplateS3Uri { get; set; }

        public OrganizationConformancePackArgs()
        {
        }
        public static new OrganizationConformancePackArgs Empty => new OrganizationConformancePackArgs();
    }
}
