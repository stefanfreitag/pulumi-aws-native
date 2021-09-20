// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DataBrew.Inputs
{

    /// <summary>
    /// Input
    /// </summary>
    public sealed class DatasetInputArgs : Pulumi.ResourceArgs
    {
        [Input("dataCatalogInputDefinition")]
        public Input<Inputs.DatasetDataCatalogInputDefinitionArgs>? DataCatalogInputDefinition { get; set; }

        [Input("databaseInputDefinition")]
        public Input<Inputs.DatasetDatabaseInputDefinitionArgs>? DatabaseInputDefinition { get; set; }

        [Input("s3InputDefinition")]
        public Input<Inputs.DatasetS3LocationArgs>? S3InputDefinition { get; set; }

        public DatasetInputArgs()
        {
        }
    }
}
