// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Kendra.Inputs
{

    public sealed class DataSourceConfluenceBlogConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("blogFieldMappings")]
        private InputList<Inputs.DataSourceConfluenceBlogToIndexFieldMappingArgs>? _blogFieldMappings;
        public InputList<Inputs.DataSourceConfluenceBlogToIndexFieldMappingArgs> BlogFieldMappings
        {
            get => _blogFieldMappings ?? (_blogFieldMappings = new InputList<Inputs.DataSourceConfluenceBlogToIndexFieldMappingArgs>());
            set => _blogFieldMappings = value;
        }

        public DataSourceConfluenceBlogConfigurationArgs()
        {
        }
        public static new DataSourceConfluenceBlogConfigurationArgs Empty => new DataSourceConfluenceBlogConfigurationArgs();
    }
}
