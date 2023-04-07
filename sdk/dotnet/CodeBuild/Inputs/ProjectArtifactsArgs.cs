// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CodeBuild.Inputs
{

    public sealed class ProjectArtifactsArgs : global::Pulumi.ResourceArgs
    {
        [Input("artifactIdentifier")]
        public Input<string>? ArtifactIdentifier { get; set; }

        [Input("encryptionDisabled")]
        public Input<bool>? EncryptionDisabled { get; set; }

        [Input("location")]
        public Input<string>? Location { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("namespaceType")]
        public Input<string>? NamespaceType { get; set; }

        [Input("overrideArtifactName")]
        public Input<bool>? OverrideArtifactName { get; set; }

        [Input("packaging")]
        public Input<string>? Packaging { get; set; }

        [Input("path")]
        public Input<string>? Path { get; set; }

        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public ProjectArtifactsArgs()
        {
        }
        public static new ProjectArtifactsArgs Empty => new ProjectArtifactsArgs();
    }
}
