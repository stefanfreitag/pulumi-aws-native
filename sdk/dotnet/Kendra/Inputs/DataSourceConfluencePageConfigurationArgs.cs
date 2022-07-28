// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Kendra.Inputs
{

    public sealed class DataSourceConfluencePageConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("pageFieldMappings")]
        private InputList<Inputs.DataSourceConfluencePageToIndexFieldMappingArgs>? _pageFieldMappings;
        public InputList<Inputs.DataSourceConfluencePageToIndexFieldMappingArgs> PageFieldMappings
        {
            get => _pageFieldMappings ?? (_pageFieldMappings = new InputList<Inputs.DataSourceConfluencePageToIndexFieldMappingArgs>());
            set => _pageFieldMappings = value;
        }

        public DataSourceConfluencePageConfigurationArgs()
        {
        }
        public static new DataSourceConfluencePageConfigurationArgs Empty => new DataSourceConfluencePageConfigurationArgs();
    }
}
